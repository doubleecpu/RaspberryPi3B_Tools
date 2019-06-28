#!/bin/bash
echo "Please enter root user MySQL password!"
read rootpasswd
dbname="SensorDB" 
echo "Please enter the WordPress database CHARACTER SET! (example: utf8, ...)"
read charset
echo "Creating new SensorDB database..."
mysql -uroot -p${rootpasswd} -e "CREATE DATABASE ${dbname} /*\!40100 DEFAULT CHARACTER SET ${charset} */;"
echo "Database successfully created!"
echo "Showing existing databases..."
echo "Please enter the NAME of the new database user! (example: pi)"
read username
echo "Please enter the PASSWORD for the new database user!"
read userpass
echo "Creating new user..."
mysql -uroot -p${rootpasswd} -e "CREATE USER ${username}@localhost IDENTIFIED BY '${userpass}';"
echo "User successfully created!"
echo "Granting ALL privileges on ${dbname} to ${username}!"
mysql -uroot -p${rootpasswd} -e "GRANT ALL PRIVILEGES ON ${dbname}.* TO '${username}'@'localhost'; FLUSH PRIVILEGES; SHOW DATABASES;"
echo "Database and User Created!"
exit