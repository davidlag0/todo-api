### Setup

* Create a .env file with the following

```
DEBUG = True
SECRET_KEY = 'dev'
```

### Format code with Black
* `pipenv run black todoapi`

### Deployment to Heroku

At least set these environment variables when deploying to Heroku:
* DISABLE_COLLECTSTATIC: 1 (`heroku config:set DISABLE_COLLECTSTATIC=1`)
* SECRET_KEY
* WEB_CONCURRENCY (`heroku config:set WEB_CONCURRENCY=3`)
* ALLOWED_HOSTS
