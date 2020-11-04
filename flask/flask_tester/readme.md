### Simple Flask app running behind Nginx & uWSGI in a Docker container

source: https://github.com/Julian-Nash/docker-flask-uwsgi-nginx-simple.git


```sh
cd app
python -m venv env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=run.py # export is 'set' on windows
export FLASK_ENV=development
flask run
```

Go to - http://127.0.0.1:5000


To run the container locally:

```sh
docker-compose up --build
```

Go to - http://127.0.0.1:8000

### Notes

`nginx` logs and `uwsgi` logs will be logged to `log/nginx` and `log/uwsgi` respectively. This can be changed by changing the `volume` mounts in the `docker-compose.yml`.

Alternatively, delete the `volumes` to have Docker log to `Stdout`.
