## Setup

* Create a .env file with the following

```
DEBUG = True
SECRET_KEY = 'dev'
```

## Development

### Install everything
* `pipenv install --dev`

### Run Development Server
* `pipenv run python manage.py runserver`

### Format code with Black
* `pipenv run black todoapi`

### Tests
* `pipenv run pytest`

### Deployment to Heroku

At least set these environment variables when deploying to Heroku:
* DISABLE_COLLECTSTATIC: 1 (`heroku config:set DISABLE_COLLECTSTATIC=1`)
* SECRET_KEY
* WEB_CONCURRENCY (`heroku config:set WEB_CONCURRENCY=3`)
* ALLOWED_HOSTS
