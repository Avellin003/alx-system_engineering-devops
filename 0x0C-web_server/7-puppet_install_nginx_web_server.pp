#installing nginx with puppet
package { 'download-nginx:'
	ensure => installed,
}
file_line { 'avellin':
	ensure => 'present',
	path   => '/etc/nginx/sites-available/default',
	after  => 'listen 80 default_server;',
	line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
file { 'index.html':
	content => 'Hello World',
}
service { 'download-nginx':
	ensure => running,
	require => Package['nginx'],
}
