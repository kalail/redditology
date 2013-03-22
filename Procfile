web: python manage.py runserver
worker: python manage.py celery worker -E --loglevel=INFO
scheduler: python manage.py celery beat
monitor: python manage.py celery flower --broker=redis://localhost:6379/0