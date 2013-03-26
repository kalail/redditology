web: python redditology/manage.py run_gunicorn --log-level=debug --workers=9 --bind=0.0.0.0:8000
worker: python redditology/manage.py celery worker -E --loglevel=DEBUG --concurrency=9
scheduler: python redditology/manage.py celery beat
monitor: python redditology/manage.py celery flower --port=5000