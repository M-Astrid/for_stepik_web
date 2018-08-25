  sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
  sudo rm -rf /etc/nginx/sites-enabled/default
  sudo /etc/init.d/nginx restart
  sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
  sudo gunicorn --config /home/box/web/etc/gunicorn.conf hello:app