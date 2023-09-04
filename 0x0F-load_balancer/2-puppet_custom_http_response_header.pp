#2-puppet_costom_http_response_header.pp

# Define a custom fact to retrieve the hostname of the server
Facter.add('server_hostname') do
  setcode 'hostname -f'
end

# Install the puppetlabs-nginx module (if not already installed)
class { 'nginx':
  ensure => 'installed',
}

# Define an Nginx location block to add the custom header
nginx::resource::location { 'custom_header_location':
  location   => '/',
  server    => 'default',
  body      => 'before $body',
  ssl       => false,
  header    => 'add_header X-Served-By $server_hostname;',
  vhost     => 'default',
  file_name => 'default',
}

# Reload Nginx to apply the configuration
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => Nginx::Resource::Location['custom_header_location'],
}

