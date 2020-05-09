#!/bin bash
echo "Starting Wordpress setup -----------------------"
cd /var/www/html/ 
sudo rm * 
sudo wget http://wordpress.org/latest.tar.gz
sudo tar xzf latest.tar.gz 
sudo mv wordpress/* .
tree -L 1 
sudo chown -R www-data: .
sudo mysql -u root -p -e "create database wordpress; GRANT ALL PRIVILEGES ON wordpress.* TO 'root'@'localhost' IDENTIFIED BY '"${rootpasswd}"'; FLUSH PRIVILEGES; \q"
echo "The WordPress website should now be running. open web browser and enter http://localhost this should open the setup-config.php webpage."
