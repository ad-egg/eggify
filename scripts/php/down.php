<?php

  echo exec('sudo rm -rf eggify/mysql/* /tmp/* 2>&1');
  echo exec('sudo docker system prune -f 2>&1');
  chdir('/home/ubuntu/eggify');
  echo exec('sudo docker-compose down');
  echo('EGGIFY DEPLOYED');

?>
