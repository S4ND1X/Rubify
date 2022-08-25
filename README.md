<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/s4nd1x/rubify">
    <img src="images/logo.png" alt="Logo" width="170" height="120">
  </a>

<h3 align="center">Rubify</h3>

  <p align="center">
    Cloud infrastructure provisioning and management tool
    <br />
    <a href="https://github.com/s4nd1x/rubify"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/s4nd1x/rubify">View Demo</a>
    ·
    <a href="https://github.com/s4nd1x/rubify/issues">Report Bug</a>
    ·
    <a href="https://github.com/s4nd1x/rubify/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
[![Rubify Landing Page][product-screenshot]](https://example.com)

Infrustructure provisioning is a critical part of today's cloud key features . We all have used some of the most popular cloud providers to provision infrastructure, like `Heroku`, `AWS`, `DigitalOcean`, `Vercel`, `Google Cloud Platform`, and others.

*But what if you want to provision programmatically infrastructure by your own? How do you even code such a thing?*

That's where Rubify comes in. Rubify is a cloud infrastructure provisioning tool that allows you to provision infrastructure programmatically. 

Made with the sole purpose of learning how these platforms work internally, and teach myself new technologies and concepts.

Using **Pulumi** allows us to dinamically create **AWS S3 buckets** to host our code, as well as create a new **AWS EC2** instance to host our application.

###Hosting
  - **Creating new sit**e
  [![Rubify Hosting Demo][hosting-screenshot]](https://example.com)

  - **AWS S3 Bucket created**
  [![Rubify Hosting Demo2][hosting-screenshot2]](https://example.com)

  - **Website deployed**
  [![Rubify Hosting Demo3][hosting-screenshot3]](https://example.com)

###Virtual Machine (VM)
  - **Creating new VM**
  [![Rubify VM Demo][vm-screenshot]](https://example.com)
  - **VM created**
  [![Rubify VM Demo2][vm-screenshot2]](https://example.com)
  - **VM deployed**
  [![Rubify VM Demo3][vm-screenshot3]](https://example.com)



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With ⛏️

* [![Python][Python.org]][Python-url]
* [![Pulumi][Pulumi.com]][Pulumi-url]
* [![AWS][AWS.com]][AWS-url]
* [![Flask][Flask.com]][Flask-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started 👶

There's a few things you'll need before running this project:
  - [ ] Have an *AWS account and AWS CLI* installed and configured
  - [ ] *Pulumi account* with stack created on dev environment
  - [ ] *Pulumi CLI* installed and configured
  - [ ] Have *venv installed* since pulumi uses virtual environments
  - [ ] Have an *ssh keypair set up* in PEM format

### Prerequisites 👓

Let's install all the tools we need to get started.

* AWS CLI (Linux x86 - 64bit )
``` bash
  curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  unzip awscliv2.zip
  sudo ./aws/install
```
*For more information on AWS CLI, see [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/userguide/installing.html)*

* Pulumi CLI
``` bash
  curl -fsSL https://get.pulumi.com | sh
```
*For more information on Pulumi CLI, see [Pulumi CLI Documentation](https://www.pulumi.com/docs/get-started/install/)*

### Installation 👨‍💻

1. Clone the repo
   ```sh
   git clone https://github.com/s4nd1x/rubify.git
   ```
2. Run pulumi up to create the venv folder 
   ```sh
   pulumi up
   ```
3. Install the dependecies inside the venv folder
   ```sh
    venv/bin/pip install flask requests python-dotenv
    venv/bin/pip install -r requirements.txt
   ```
4. Create .env file inside root directory
    ```sh
      SECRET_KEY="<random string>"
      PROJECT_NAME="<pulumi project name>"
      PULUMI_ORG="<pulumi organization name>"
    ```
5. Make sure you have ssh keypair set up in PEM format
    ```sh
      ssh-keygen -m PEM
      cd ~/.ssh
      mv id_rsa id_rsa.pem
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage ❓

Once you have installed all the previous requirements, you should be able to run the following commands:

* Run the app
  ```sh
   FLASK_RUN_PORT=1337 FLASK_ENV=development venv/bin/flask run
  ```
* You should be able to access the app at the following url:
  ```sh
   http://localhost:1337
  ```

**You're all set! 🚀**

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap 🗺️

This is a work in progress and I'm still learning how does Pulumi works so this are the things I'm planning to add:

- [ ] Host other types of content (images, videos, etc) not only HTML
- [ ] Be able to decide wich OS to use for the VM
- [ ] Have an ssh built-in into the web app

See the [open issues](https://github.com/s4nd1x/rubify/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing 🏗️

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License 📜

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact ☎️

Jorge Sanchez - [@s4nd1x](https://twitter.com/s4nd1x) - georgesanchez.diazjr@gmail.com

Project Link: [https://github.com/s4nd1x/rubify](https://github.com/s4nd1x/rubify)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments 📣

* [@marleneharms](https://github.com/marleneharms) for showning me the original idea of the project
* [@freecodecamp](https://github.com/freecodecamp) for the guide on which this project was built
* [@sebastiancrossa](https://github.com/sebastiancrossa) for the advice on where to host the app

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/s4nd1x/rubify.svg?style=for-the-badge
[contributors-url]: https://github.com/s4nd1x/rubify/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/s4nd1x/rubify.svg?style=for-the-badge
[forks-url]: https://github.com/s4nd1x/rubify/network/members
[stars-shield]: https://img.shields.io/github/stars/s4nd1x/rubify.svg?style=for-the-badge
[stars-url]: https://github.com/s4nd1x/rubify/stargazers
[issues-shield]: https://img.shields.io/github/issues/s4nd1x/rubify.svg?style=for-the-badge
[issues-url]: https://github.com/s4nd1x/rubify/issues
[license-shield]: https://img.shields.io/github/license/s4nd1x/rubify.svg?style=for-the-badge
[license-url]: https://github.com/s4nd1x/rubify/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jorgesanchezdiaz

<!-- Images -->
[product-screenshot]: images/screenshot.png
[hosting-screenshot]: images/screenshot_2.png
[hosting-screenshot2]: images/screenshot_3.png
[hosting-screenshot3]: images/screenshot_4.png
[vm-screenshot]: images/screenshot_5.png
[vm-screenshot2]: images/screenshot_6.png
[vm-screenshot3]: images/screenshot_7.png


<!-- Badges -->
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[AWS.com]: https://img.shields.io/badge/AWS-orange?style=for-the-badge&logo=aws&logoColor=white
[AWS-url]: https://aws.amazon.com
[Pulumi.com]: https://img.shields.io/badge/Pulumi-purple?style=for-the-badge&logo=pulumi&logoColor=white
[Pulumi-url]: https://pulumi.com
[Python.org]: https://img.shields.io/badge/Python-green?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Flask.com]: https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com

