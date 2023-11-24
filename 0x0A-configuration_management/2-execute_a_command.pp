# kill_process.pp

exec { 'kill_process':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',
}