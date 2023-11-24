# Manifest that kills a process

exec { 'pkill -f 'killmenow':
    path  => '/usr/bin'
}