#!/bin/bash 
python manage.py migrate 
gunicorn backend.wsgi:application 
