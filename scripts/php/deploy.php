<?php

  echo exec('sudo rm -rf eggify/mysql/* /tmp/* 2>&1');
  echo exec('sudo docker system prune -f 2>&1');
  chdir('/home/ubuntu/eggify');
  echo exec('sudo cp -r eggify/static /var/www/html 2>&1');
  echo exec('sudo docker-compose up -d 2>&1');
  echo('EGGIFY DEPLOYED');

?>
