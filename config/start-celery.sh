#!/bin/sh

# Start Celery worker in the background
celery celery --app=config worker --loglevel=info   &

# Start Celery beat
celery -A worker beat --loglevel=info
