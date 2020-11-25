#!/bin/bash

echo "Starting Update -----------------------"
sudo apt-get update -y
echo "Starting Upgrade -----------------------"
sudo apt-get upgrade -y
echo "autoremoving -----------------------"
sudo apt autoremove -y
echo "Installing Apache Webserver -----------------------"
sudo apt-get install apache2 -y

echo "Testing Apache on Raspberry Pi -----------------------"
wget -O check_apache.html http://127.0.0.1 
echo "Installing PHP -----------------------"
sudo apt install php php-mbstring php-cli php-gd libapache2-mod-php php-cgi -y

echo "Installing MariaDb -----------------------"
echo -n "Please enter root user MySQL password!"
read -s rootpasswd
echo
sudo apt-get install mariadb-server php-mysql -y
sudo service apache2 restart
sudo mysql_secure_installation

echo "Changing ownership to pi user -----------------------"
cd /var/www/html
sudo chown -R pi:www-data /var/www/html/*
sudo chmod -R 755 /var/www/html/*
sudo rm index.html
sudo touch index.php
echo "Please Add Test Message To index.php -----------------------"
sudo echo "<?php phpinfo(); ?>" >> /var/www/html/index.php
#sudo nano index.php
wget -O check_php.html http://127.0.0.1 
echo "Restaring apache service -----------------------"
sudo service apache2 restart
echo "Installing PHP Admin Please Configure Database -------------" 
sudo apt-get install phpmyadmin -y
sudo mysql -u root -p${rootpasswd} -e "use mysql; update user set plugin='' where User='root'; flush privileges; \q"
sudo mysql -u root -p${rootpasswd} -e "GRANT ALL PRIVILEGES ON mysql.* TO 'root'@'localhost'; FLUSH PRIVILEGES; SHOW DATABASES;"
echo "Database and User Created!"
echo "adjusting PHP configuration  -------------"
cd /etc/apache2/conf-available
sudo ln -s ../../phpmyadmin/apache.conf phpmyadmin.conf
cd /etc/apache2/conf-enabled
sudo ln -s ../conf-available/phpmyadmin.conf phpmyadmin.conf
sudo service apache2 restart
