<?php

    echo exec("sudo puppet module install garethr-docker 2>&1");
    chdir('/var/www/html/scripts/puppet');
    echo exec("sudo puppet apply provision.pp 2>&1");

?>
