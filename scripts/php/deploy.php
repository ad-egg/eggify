<?php

  echo exec('git clone https://github.com/ad-egg/eggify.git');
  echo exec('sudo minikube start 2>&1');
  echo exec('sudo kubectl run eggify --image=sazad44/egg:v1 --port=8080 2>&1');
  echo exec('sudo kubectl proxy');
  echo exec('export POD_NAME=sudo kubectl get pods | tail -1 | cut -d " " -f 1');
  /*echo exec('cd eggify && sudo kubectl exec $POD_NAME gunicorn --bind 0.0.0.0:8030 egg_clusters.wsgi');*/
  echo('EGGIFY DEPLOYED');

?>
