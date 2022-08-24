from inspect import stack
import json
import site
import requests
from flask import (
    current_app,
    Blueprint,
    request,
    flash,
    redirect,
    url_for,
    render_template,
)

import pulumi
import pulumi.automation as auto
from pulumi_aws import s3

bp = Blueprint("sites", __name__, url_prefix="/sites")

def create_pulumi_program(content: str):
    """
    Create a website using an s3 bucket based on the content the user provided
    """
    #create a bucket and expose a website index document
    site_bucket = s3.Bucket(
        "s3-website-bucket", website=s3.BucketWebsiteArgs(index_document="index.html")
    )
    index_content = content

    # Write the index.html file to the bucket
    s3.BucketObject(
        "index",
        bucket=site_bucket.id,
        content=index_content,
        key="index.html",
        content_type="text/html; charset=utf-8",
    )

    # Set the acces policy for the bucket so all objects can be read
    s3.BucketPolicy(
        "bucket-policy",
        bucket=site_bucket.id,
        policy=site_bucket.id.apply(
            lambda bucket_id: json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": {
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": ["s3:GetObject"],
                        # Policy refers to the bucket explicitly
                        "Resource": [f"arn:aws:s3:::{bucket_id}/*"],
                    },
                }
            )
        ),
    )

    # Export the website URL
    pulumi.export("website_url", site_bucket.website_endpoint)
    pulumi.export("website_content", index_content)


@bp.route("/new", methods=["GET", "POST"])
def create_site():
    """
    Create a new website based on the content the user provided
    """
    if request.method == "POST":
        stack_name = request.form.get("site-id")
        file_url = request.form.get("file-url")
        if file_url:
            site_content = requests.get(file_url).text
        else:
            site_content = request.form.get("site-content")
        
        def pulumi_program():
            return create_pulumi_program(str(site_content))

        try:
            # create a new stack, generating our plumi program on the fly from the post body
            stack = auto.create_stack(
                stack_name=str(stack_name),
                project_name=current_app.config["PROJECT_NAME"],
                program=pulumi_program,
            )
            stack.set_config("aws:region", auto.ConfigValue("us-east-1"))
             # deploy the stack, tailing the logs to stdout
            stack.up(on_output=print)

            flash(
                f"Successfully created site '{stack_name}'", 
                category="success"
            )
        except auto.StackAlreadyExistsError:
            flash(
                f"Error: Site with name '{stack_name}' already exists, pick a unique name", 
                category="danger"
            )

        return redirect(url_for("sites.list_sites"))

    return render_template("sites/create.html")


@bp.route("/", methods=["GET"])
def list_sites():
    """
    List all the sites that have been created
    """
    sites = []
    org_name = current_app.config["PULUMI_ORG"]
    project_name = current_app.config["PROJECT_NAME"]
    try:
        ws = auto.LocalWorkspace(
            project_settings=auto.ProjectSettings(
                name=project_name, runtime="python")
        )
        all_stacks = ws.list_stacks()
        for stack in all_stacks:
            stack = auto.select_stack(
                stack_name=stack.name,
                project_name=project_name,
                # no-op program, just to get ouputs
                program=lambda: None,
            )
            outs = stack.outputs()
            if 'website_url' in outs:
                sites.append(
                    {
                        "name": stack.name,
                        "url": f"https://{outs['website_url'].value}",
                        "content": f"https://app.pulumi.com/{org_name}/{project_name}/{stack.name}",
                    }
                )
    except Exception as exn:
        flash(str(exn), category="danger")
    
    return render_template("sites/index.html", sites=sites)


@bp.route("/<string:id>/update", methods=["GET", "POST"])
def update_site(id: str):
    stack_name = id

    if request.method == "POST":
        file_url = request.form.get("file-url")
        if file_url:
            site_content = requests.get(file_url).text
        else:
            site_content = str(request.form.get("site-content") )  

        try:
            def pulumi_program():
                return create_pulumi_program(str(site_content)) 
            
            stack = auto.select_stack(
                stack_name=stack_name,
                project_name=current_app.config["PROJECT_NAME"],
                program=pulumi_program,
            )
            stack.set_config("aws:region", auto.ConfigValue("us-east-1"))
            # deploy the stack, tailing the logs to stdout
            stack.up(on_output=print)
            flash(f"Site '{stack_name}' successfully updated", category="success")
        
        except auto.ConcurrentUpdateError:
            flash(f"Error: Site '{stack_name}' is currently updating", category="danger")
    
        except Exception as exn:
            flash(str(exn), category="danger")
        return redirect(url_for("sites.list_sites"))
    
    stack = auto.select_stack(
        stack_name=stack_name,
        project_name=current_app.config["PROJECT_NAME"],
        # no-op program, just to get ouputs
        program=lambda: None,
    )
    outs = stack.outputs()
    content_output = outs.get("website_content")
    content = content_output.value if content_output else None
    return render_template("sites/update.html", site=stack_name, content=content)

@bp.route("/<string:id>/delete", methods=["POST"])
def delete_site(id: str):
    stack_name = id

    try:
        stack = auto.select_stack(
            stack_name=stack_name,
            project_name=current_app.config["PROJECT_NAME"],
            # no-op program, just to get ouputs
            program=lambda: None,
        )
        stack.destroy(on_output=print)
        stack.workspace.remove_stack(stack_name)
        flash(f"Site '{stack_name}' successfully deleted", category="success")
    except auto.ConcurrentUpdateError:
        flash(f"Error: Site '{stack_name}' is currently updating", category="danger")
    except Exception as exn:
        flash(str(exn), category="danger")
    
    return redirect(url_for("sites.list_sites"))
