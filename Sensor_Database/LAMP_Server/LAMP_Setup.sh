#!/bin bash
UPDATE_COMPLETE= false
 UPGARDE_COMPLETE= false
 AUTOREMOVE_COMPLETE= false
 echo "Starting Update -----------------------"
 apt-get update
 echo "Starting Upgrade -----------------------"
 apt-get upgrade
 echo "autoremoving -----------------------"
 apt autoremove -y
 echo "Installing Apache Webserver -----------------------"
 sudo apt-get install apache2 -y
 echo "Changing ownership to pi user -----------------------"
 sudo chown -R pi:www-data /var/www/html/ 
 sudo chmod -R 770 /var/www/html/
 echo "Testing Apache on Raspberry Pi -----------------------"
 wget -O check_apache.html http://127.0.0.1 
 echo "Installing MariaDb -----------------------"
 sudo apt-get install mysql-server -y
 echo "Installing PHP -----------------------"
 sudo apt install php php-mbstring php-mysql php-cli php-gd libapache2-mod-php php-cgi -y
 cd /var/www/html
 sudo rm index.html
 sudo touch index.php
 echo "Please Add Test Message To index.php -----------------------"
 echo "echo “<?php phpinfo ();?>” > /var/www/html/index.php"
 sudo nano index.php
 
 echo "Restaring apache service -----------------------"
 sudo service apache2 restart
 echo "Installing PHP Admin Please Configure Database -------------" 
 sudo apt install phpmyadmin -y
 sudo mysql -u root
 use mysql; update user set plugin='' where User='root'; flush privileges; \q 
 mysql_secure_installation
