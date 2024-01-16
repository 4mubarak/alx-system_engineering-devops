# Fix 500 error when to GET the HTTP method is requested to the Apache web server

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
