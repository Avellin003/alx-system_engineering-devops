#web_stack-debugging_4

exec {'repl':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'re-tart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
