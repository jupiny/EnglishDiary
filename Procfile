web: gunicorn --pythonpath english_diary/ --bind :5736 --workers=3 english_diary.wsgi
worker: celery --workdir=english_diary/ --app=english_diary.celery:app --concurrency=3 worker
flower: celery --workdir=english_diary/ --app=english_diary.celery:app flower
