#Puppet resource to increase file open limit

exec {'replace':
  command  =>  'sed -i "s/^holberton hard.*/holberton hard nofile 2048/" /etc/security/limits.conf',
  path     =>  '/bin',
  provider =>   'shell',
}

exec {'replacement':
  command  => 'sed -i "s/^holberton soft.*/holberton soft nofile 1024/" /etc/security/limits.conf',
  path     =>  '/bin',
  provider =>   'shell',
}
