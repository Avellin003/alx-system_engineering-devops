# the puppet script

file {'copy_file':
  ensure => file,
  source => '/var/www/html/wp-includes/class-wp-locale.php',
  path   => '/var/www/html/wp-includes/class-wp-locale.phpp',
}
