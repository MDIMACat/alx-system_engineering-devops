# Create a file in the /tmp dir with specific options

file {'/tmp/school' :
    ensure  => 'file',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
    mode    => '0744'
}