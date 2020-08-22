# fastapi-starter-template


##  Description

This is a basic python api setup using the FastAPI framework. It is deployable to the cloud out of the box without much configuration or changes needed (if any at all).

###  Directory Structure
```
fastapi-starter-template
├── app
│   ├── api
│   │   ├── endpoints
│   │   │   ├── __init__.py
│   │   │   └── hello.py
│   │   └── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   └── application.py
│   ├── __init__.py
│   └── main.py
├── tests
│   ├── endpoints
│   │   └── hello_test.py
│   ├── __init__.py
│   └── conftest.py
├── Dockerfile
├── README.md
├── docker-compose.yaml
├── poetry.lock
├── pyproject.toml
└── tox.ini
```

###  Features

-  Logging

-  Testing & Coverage

-  REST API support

-  Automatic API documentation

-  Pre-Commit Code Linting & Formatting

##  Getting Started

Getting started developing with this template is pretty simple using docker and docker-compose.

```shell script
# Clone the repository
git clone git@github.com:zdmwi/fastapi-starter-template.git

# cd into project root
cd fastapi-starter-template

# Launch the project
docker-compose up
```

Afterwards, the project will be live at [http://localhost:5000](http://localhost:5000).

## Documentation

FastAPI automatically generates documentation based on the specification of the endpoints you have written. You can find the docs at [http://localhost:5000/docs](http://localhost:5000/docs).

## Testing

In order to test and lint the project locally you need to install the poetry dependencies outlined in the pyproject.toml file.

If you have Poetry installed then it's as easy as running `poetry shell` to activate the virtual environment first and then `poetry install` to get all the dependencies.

This starter template has an example test which covers its only endpoint. To run the test, ensure you are
in the same directory as the `tox.ini` file and run `tox` from the command line. It will also perform code
linting and formatting as long as the pre-commit hooks were installed. We'll talk about that next.

# Code Formatting & Linting

To activate pre-commit formatting and linting all you need to do is run `pre-commit install` from the root of your local git repository. Now
every time you try to make a commit, the code will be formatted and linted for errors first.
