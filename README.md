# Simple products review applicaiton using django

This application houses a list of products that can be reviewed by users. An admin can apply CRUD operations on products while a user can review products only if logged in.

## Requirements

- python 3.8.1
- django 3.0.3
- sqlite 3.24.0

## Setup

Navigate to project folder and run the following to start the virtual environment:

    source bin/activate

Inside the project folder run the following command to install all requirements:

    pip3 install -r requirements.txt

Navigate to the src/ folder inside the project folder and run the following command:

    python3 manage.py makemigrations
    python3 manage.py migrate

Create your super user account with the following command inside the src/ directory:

    python3 manage.py createsuperuser

Run the Python dev server with the following command inside the src/ directory:

    python3 manage.py runserver