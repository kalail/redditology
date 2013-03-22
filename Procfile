web: python redditology/manage.py run_gunicorn --workers=9 --bind=0.0.0.0:80
worker: python redditology/manage.py celery worker -E --loglevel=INFO
scheduler: python redditology/manage.py celery beat
monitor: python redditology/manage.py celery flower