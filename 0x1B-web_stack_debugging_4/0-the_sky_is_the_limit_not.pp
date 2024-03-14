# file to replace

exec {'replace':
  command  =>  'sed -i "s/^ULIMIT.*/ULIMIT=\"-n 2048\"/" /etc/default/nginx',
  path     =>  '/bin',
  provider =>   'shell'
}

#restarting the nginx
exec {'restart':
  command =>  'nginx restart',
  path    =>  '/etc/init.d',
  require =>  Exec['replace']
}
