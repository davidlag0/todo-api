## Setup

* Create a .env file with the following

```
DEBUG = True
SECRET_KEY = 'dev'
```

## Development

### Create pyenv virtual environment and install pipenv
* `pyenv virtualenv 3.9.9 todo-api`
* `python -m pip install pipenv`
* Reload shell

### Install dependencies
* `pipenv install --dev`

### Run Development Server
* `pipenv run python manage.py runserver`

### Format code with Black
* `pipenv run black todoapi`

### Tests
* `pipenv run pytest`

### Security Checks with Bandit
* `pipenv run bandit -r todoapi`

### Deployment to Heroku

At least set these environment variables when deploying to Heroku:
* DISABLE_COLLECTSTATIC: 1 (`heroku config:set DISABLE_COLLECTSTATIC=1`)
* SECRET_KEY
* WEB_CONCURRENCY (`heroku config:set WEB_CONCURRENCY=3`)
* ALLOWED_HOSTS

### Tools
* Dependency Management: `pipenv`
* Code Formatting: `black`
* Style Enforcement: `pylint`
* Type Checking: `mypy`
* Testing: `pytest`
* Code Coverage: `coverage`
* Security Checks: `bandit`, `safety` and `dodgy`
