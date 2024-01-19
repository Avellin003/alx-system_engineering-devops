exec { 'killmenow':
  path    => '/bin/',
  command => 'pkill killmenow',
  returns => [0, 1]
}
