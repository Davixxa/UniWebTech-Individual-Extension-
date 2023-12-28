# GAMEX - Reimplemented
A reimplementation of the PHPVideoGameLibrary repository in a different framework.

# Requirements

* Python 3.11
* Virtual Environments
* MariaDB (Or any compatible SQL server, like MySQL)

# Installation & Running the Development Server

## Step 1: Create a new virtual environment. 
`python -m venv /path/to/new/virtual/environment`

## Step 2: Activate said virtual environment:

Windows: `C:\> <venv>\Scripts\activate.bat`
Mac/Linux/BSD `$ source <venv>/bin/activate`

## Step 3: Install the dependencies:
In the activated virtual envrironment, install the dependencies using pip
`pip install -r requirements.txt`

## Step 4: Configure your settings.py and databases
[Reference the Django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/)

## Step 5: Run the development server like you would with any Django project.
`python manage.py runserver`
