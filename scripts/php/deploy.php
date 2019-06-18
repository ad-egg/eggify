<?php

  echo exec('sudo git clone https://github.com/ad-egg/eggify.git');
  echo exec('sudo rm -rf eggify/mysql/* /tmp/* 2>&1');
  echo exec('sudo docker system prune -f 2>&1');
  chdir('/var/www/html/eggify');
  echo exec('sudo kompose convert');
  echo exec('sudo kompose up');
  echo('EGGIFY DEPLOYED');

?>
