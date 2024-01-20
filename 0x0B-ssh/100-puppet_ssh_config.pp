#!/usr/bin/env bash
#automation to make changes on configfile
file { 'etc/ssh/ssh_config':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => "IdentityFile ~/.ssh/school\n\tPasswordAuthentication no"
}
