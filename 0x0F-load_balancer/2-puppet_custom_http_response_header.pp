# Update package repositories
exec { 'updating':
  command  => 'sudo apt-get -y update',
}

# Check if Nginx is installed
exec { 'check_nginx_installed':
  command     => 'dpkg -l | grep nginx',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  notify      => Package['nginx'],
}

# Install Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['updating'],
}

# Modify Nginx configuration file
file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => template('your_module/nginx.conf.erb'), # Create a template with the desired content
  notify  => Service['nginx'],
}

# Add a custom header to Nginx configuration
file_line { 'add_custom_header':
  path    => '/etc/nginx/nginx.conf',
  line    => 'add_header X-Served-By "${hostname}";',
  require => File['/etc/nginx/nginx.conf'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}

# Restart Nginx if configuration changes
exec { 'restart_nginx':
  command     => 'sudo service nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/nginx/nginx.conf'],
}
