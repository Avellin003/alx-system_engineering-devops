#installation of the nginx
exec {'updating':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'Nginx installation':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

exec { 'header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";
/" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

exec { 'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
