#!/bin bash
echo "Starting Update -----------------------"
apt-get update -y
echo "Starting Upgrade -----------------------"
apt-get upgrade -y
echo "autoremoving -----------------------"
apt autoremove -y
echo "Installing Apache Webserver -----------------------"
sudo apt-get install apache2 -y

echo "Testing Apache on Raspberry Pi -----------------------"
wget -O check_apache.html http://127.0.0.1 
echo "Installing MariaDb -----------------------"
sudo apt-get install mariadb-server -y
sudo mysql_secure_installation
sudo mysql -u root -p 
use mysql; update user set plugin='' where User='root'; flush privileges; \q 
echo "Installing PHP -----------------------"
sudo apt install php php-mbstring php-mysql php-cli php-gd libapache2-mod-php php-cgi -y

echo "Changing ownership to pi user -----------------------"
cd /var/www/html
sudo chown -R pi:www-data /var/www/html/*
sudo chmod -R 770 /var/www/html/*
sudo rm index.html
sudo touch index.php
echo "Please Add Test Message To index.php -----------------------"
sudo echo "<?php phpinfo(); ?>" >> /var/www/html/index.php
sudo nano index.php

echo "Restaring apache service -----------------------"
sudo service apache2 restart
echo "Installing PHP Admin Please Configure Database -------------" 
sudo apt install phpmyadmin -y

cd /etc/apache2/conf-available
sudo ln -s ../../phpmyadmin/apache.conf phpmyadmin.conf
cd /etc/apache2/conf-enabled
sudo ln -s ../conf-available/phpmyadmin.conf phpmyadmin.conf
sudo service apache2 restart
