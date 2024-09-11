# Portfolio Website

This is a website for building an online portfolio. It contains at least the following pages: Introduction, Projects, Working/Teaching, CV/Resume.
It has been developed using a Flask template available at https://github.com/a-hamza-r/flask-init-mini.

## Running it locally
To run the website locally, carry out the following steps:

First clone the repository (you need to have git installed):
```
git clone git@github.com:a-hamza-r/portfolio.git
```

Then navigate to the directory:
```
cd portfolio
```

Potentially, you can make changes to the website by editing the files in the repository. To get some instructions about how to make changes, check the below section "Making Changes".

There are two ways to run the website locally:
1. Using Docker
2. Using Python

### Using Docker
Make sure you have Docker installed on your machine. 
Use the Dockerfile to build the image:
```
docker build -t portfolio .
```

Then run the image:
```
docker run -p 8080:8080 portfolio
```

The website will be available at http://localhost:8080/.

### Using Python
Make sure you have Python (python3) installed on your machine. It is recommended to create a virtual environment to install the required packages.

Create a virtual environment:
```
python3 -m venv venv
```
Activate the virtual environment:
```
source venv/bin/activate
```

Install the required packages:
```
python -m pip install -r app/requirements.txt
```

Run the website:
```
export FLASK_APP=app/run.py
flask run
```

The website will be available at a local address that will be displayed in the terminal, something like http://127.0.0.1:5000/. Copy and paste this address in your browser to view the website.

## Making Changes

To make changes to the website, you can edit the files in the repository.
The website is built using Flask, a Python web framework. 
The directory app/ contains the files/code for the website.
The main file is app/run.py, which contains the routes for the website. The routes are defined using the Flask.
Inside the app/ directory, the HTML files are in the templates/ directory. The CSS and JavaScript files are in the static/ directory. The data for the website is in the data/ directory.
If you have experience with Flask framework, and HTML, CSS, JavaScript, you can make changes to the website as you like and run it locally to see the changes. You can also add new pages, new data, new styles, etc.
Otherwise, it is recommended to just edit the data in the data/ directory to add your own information. The data is in JSON format, and you can edit the files using a text editor. The data is then used to render the HTML templates.

## Deploying the Website
The website can be deployed to a server to make it available online. There are many ways to deploy a Flask website. Many deployment options are available, but usually are not free. If you have a server, you can deploy the website on it. If you have a domain name, you can link the domain to the server.
One can use Github Pages to deploy the website. However, Github Pages does not support Flask directly, so the website will need to be converted to a static website. This can be done using Frozen-Flask, which is a Flask extension that converts a Flask website to a static website. The static website can then be deployed to Github Pages.
The Frozen-Flask requirement is already installed using the requirements.txt file in the previous step.
The repository contains a directory called `static_website/` which contains the static website generated using Frozen-Flask. If you do not want to deal with all above technicalities, you can just copy the contents of this directory to your own repository and deploy it to Github Pages. You can then edit the data in the data/ directory to add your own information to the website.
To convert the website to a static website, do the following steps:

1. Inside the app/ directory, create a new config file with name `.config.yml` (note the dot at the beginning of the name). The file should contain the following:
```
path_to_static_webiste: "/path/to/your/static/website"
```
Replace "/path/to/your/static/website" with the path to the directory where you want to save the static website. For example, you can create a new directory inside the app/ directory to save the static website there.

2. Run the following command, inside the app/ directory. This will convert the website to a static website and save it in the directory specified in the config file:
```
python freeze.py
```

3. The static website will be saved in the directory specified in the config file. You can then deploy the static website to Github Pages. For more information about how to deploy a static website to Github Pages, check the following link: https://pages.github.com/.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any queries, contact me at https://a-hamza-r.github.io/contact/.
