<?php

  chdir('/home/ubuntu');
  echo exec ('sudo wget https://apt.puppetlabs.com/puppet6-release-xenial.deb 2>&1');
  echo exec('sudo dpkg -i puppet6-release-xenial.deb 2>&1');
  echo exec('sudo apt-get update 2>&1');
  echo exec('sudo apt-get -y install puppet-agent 1>&1');
  echo exec('sudo rm -rf puppet* 2>&1');
  echo exec('sudo ln -s /opt/puppetlabs/bin/puppet /usr/bin/puppet');
  echo exec('sudo apt-get -y install puppet-lint');
  echo('PUPPET INSTALLED 1>&1');

?>
