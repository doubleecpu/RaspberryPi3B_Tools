#!bin/bash
echo "Install Pure-FTPd ---------------------------"
sudo apt install pure-ftpd
#echo "Creating New User ftpuser in Group ftpgroup -"
#sudo groupadd ftpgroup
#sudo useradd ftpuser -g ftpgroup -s /sbin/nologin -d /dev/null

#sudo mkdir /home/pi/FTP
#sudo chown -R ftpuser:ftpgroup /home/pi/FTP

echo "Adding User pi in ww-data group to FTP-------"
sudo pure-pw useradd upload -u pi -g www-data -d /var/www/html/ -m
echo "Setting up virtual db------------------------"
sudo pure-pw mkdb
echo "Linking authentication file------------------"
sudo ln -s /etc/pure-ftpd/conf/PureDB /etc/pure-ftpd/auth/5puredb
echo "Restarting ftp service ----------------------"
sudo service pure-ftpd restart

cd /etc/pure-ftpd/conf/
sudo touch ChrootEveryone
echo "yes" > ChrootEveryone
sudo touch NoAnonymous
echo "yes" > NoAnonymous
sudo touch AnonymousCantUpload 
echo "yes" > AnonymousCantUpload
sudo touch AnonymousCanCreateDirs 
echo "no" > AnonymousCanCreateDirs
sudo touch DisplayDotFiles 
echo "no" > DisplayDotFiles
sudo touch DontResolve 
echo "yes" > DontResolve
sudo touch ProhibitDotFilesRead
echo "yes" > ProhibitDotFilesRead
sudo touch ProhibitDotFilesWrite 
echo "yes" > ProhibitDotFilesWrite
sudo touch FSCharset
echo "UTF-8" > FSCharset
echo "Restarting FTP Server ----------------------"
sudo service pure-ftpd restart
