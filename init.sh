  sudo ln -sf /home/astrid/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
  sudo rm -rf /etc/nginx/sites-enabled/default
  sudo /etc/init.d/nginx restart