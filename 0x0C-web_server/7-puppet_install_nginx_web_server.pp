nstall Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx service to start on boot and ensure it is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Create Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => "
server {
    listen 80;
    server_name _;

    location /redirect_me {
        return 301 http://example.com/;
    }

    location / {
        root   /var/www/html;
        index  index.html;
    }
}
",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create the HTML file for root directory
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

