# Fixing the number of failed requests to get to 0

# Increase the value in the default file of nginx of ULIMIT
exec { 'fix--for-nginx':
  # Modify the value
  command => '/bin/sed -i "s/15/4096" /etc/default/nginx',
  # Determine the path to it
  path => '/usr/local/bin/:/bin/',
}

# Restart
exec { 'nginx-restart':
  # Restarting
  command => '/etc/init.d/nginx restart',
  # Determine the path
  path => '/etc/init.d/',
}
