# Simple products review applicaiton using django

This application houses a list of products that can be reviewed by users. An admin can apply CRUD operations on products while a user can review products only if logged in.

## Requirements

- conda 4.12.0

## Setup

Navigate to project folder and run the following to install the requirements:

    conda env create -f environment.yaml

Inside the project folder run the following command to activate the environment:

    conda activate django-product-review-app

Navigate to the src/ folder inside the project folder and run the following command for creating all database migrations:

    python3 manage.py migrate

Create your super user account with the following command inside the src/ directory:

    python3 manage.py createsuperuser

## Tests

Run all tests with the follwing command inside the src/ directory:

    python3 manage.py test

To run a test for a specific module use the following command inside the src/ directory and replace `<module_name>` with the name of the module you want to run the test for such as `products`:

    python3 manage.py test <module_name>

## Launch App

Run the Python dev server with the following command inside the src/ directory:

    python3 manage.py runserver