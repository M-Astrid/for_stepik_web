  sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
  sudo rm -rf /etc/nginx/sites-enabled/default
  sudo /etc/init.d/nginx restart
  sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:app
  sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:app