# Text Extraction

## Pre-requisites

* [Python](https://www.python.org/downloads/)
* [pip](https://pypi.org/project/pip/)

## System Under Test

The different frameworks that are tested are:

* [Amazon Textract](https://aws.amazon.com/textract/)

This requires your Amazon credentials to be stored in `~/.aws/credentials.`.  
If the credentials are not found, the following exception will be thrown: `botocore.exceptions.NoCredentialsError: Unable to locate credentials`.

* 

## Build and Test

We use a project structure similar to the one described [here](https://realpython.com/python-application-layouts/#application-with-internal-packages):

    |_ bin
    |_ docs
    |_ <<application package>>
    |_ tests
        |_ features
            |_ <<scenario>>.feature
            |_ steps
    |_ .gitignore
    |_ README.md
    |_ requirements.txt
    |_ setup.py

We use [behave](https://behave.readthedocs.io/en/latest/) for BDD.

* Create a virtual environment

This step is required if you don't want to install the dependencies globally.

> `python3 -m venv .venv`  
> `source .venv/bin/activate`

* Upgrade `pip` if required

If you get a warning message, then you can upgrade `pip`:

> `cd bin`
> `python3 -m pip install --upgrade pip`

* Download dependencies

> `pip install -r requirements.txt`

* Run BDD tests

> `behave --no-capture`

* Deactivate virtual environment

> `deactivate`
