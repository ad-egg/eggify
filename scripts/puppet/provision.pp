package { ['apt-transport-https', 'ca-certificates', 'curl', 'software-properties-common'] :
  ensure => 'present'
}

package { ['virtualbox', 'virtualbox-ext-pack'] :
  ensure => present
}

exec { 'add docker official gpg key' :
  command    => '/usr/bin/curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -'
}

exec { 'add kube key' :
  command => '/usr/bin/curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | /usr/bin/apt-key add -'
}

file { 'kubernetes.list' :
  path => '/etc/apt/sources.list.d/kubernetes.list',
  ensure => 'present',
  content => 'deb http://apt.kubernetes.io/ kubernetes-xenial main'
}

$addrepcmd = @("ADDREP"/L)
  /usr/bin/add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" | /usr/bin/tee /etc/apt/sources.list.d/docker.list
  | ADDREP

exec { 'add repo' :
  command    => $addrepcmd
}

exec { 'update' :
  command => '/usr/bin/apt-get update'
}

package { 'docker-ce=18.06.3~ce~3-0~ubuntu' :
  ensure => present
}

exec { 'docker-compose install' :
  command => '/usr/bin/curl -L https://github.com/docker/compose/releases/download/1.24.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && /bin/chmod +x /usr/local/bin/docker-compose'
}

package { 'kubectl' :
  ensure => 'present'
}

exec { 'minikube' :
  command => '/usr/bin/curl -Lo minikube https://storage.googleapis.com/minikube/releases/v1.1.1/minikube-linux-amd64 && /bin/chmod +x minikube && /bin/mv minikube /usr/local/bin/'
}

exec { 'minikube driver none' :
  command => '/usr/local/bin/minikube config set vm-driver none && /bin/systemctl enable docker && /bin/systemctl start docker'
}
