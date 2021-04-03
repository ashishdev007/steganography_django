# (cd steganography/server; 
(python manage.py makemigrations;
python manage.py migrate;
gunicorn server.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"