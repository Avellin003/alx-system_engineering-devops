#!/usr/bin/env bash
#automation to make changes on configfile
file { 'etc/ssh/ssh_config':
	ensure  => present,
  content =>"
	#SSH configuration for client
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthenticatino no
",
}
