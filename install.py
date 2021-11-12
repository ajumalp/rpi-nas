# Developed by Ajmal Muhammad P 
# Contact me @ ajumalp@gmail.com
# https://owner.erratums.com
# Date created: 03-Sep-2021

# Make sure you are the root user. If not type sudo -i for that 

# We need to update and upgrade all existing packages before installing other softwares
sudo apt update && sudo apt -y upgrade

# Instal Apache server
sudo apt -y install apache2

# Install PHP Server
sudo apt -y install php libapache2-mod-php
# Give full access
chmod 777 /var/www/html/
# Move to localhost folder 
cd /var/www/html/
# Download sample php file [index.php]
wget -nc https://erratums.com/projects/rpi/index.php
cd

# Install MySQL [MariaDB] Server
sudo apt -y install mariadb-server
mysqladmin --user=root password "password"

# Install PHPMyAdmin
sudo apt -y install phpmyadmin
# We also need to install PHP MySQLi
sudo phpenmod mysqli
# Restart Apache Server 
sudo service apache2 restart
# Move the PHPMyAdmin to /usr/share folder
sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin

# Install FTP Server 
sudo apt -y install pure-ftpd
# sudo service pure-ftpd restart

# Install Samba Server
sudo apt -y install samba samba-common-bin
# Set password for Samba user 
sudo smbpasswd -a pi
# sudo systemctl restart smbd

# Finally onace again update and upgrade all packages to ensure we have installed all latest packages 
sudo apt update && sudo apt -y upgrade
