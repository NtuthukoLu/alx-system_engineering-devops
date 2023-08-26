# script too execute a command using puppet
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
