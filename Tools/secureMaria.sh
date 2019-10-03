#!/bin/bash

MYSQL_ROOT_PASSWORD=abcd1234

SECURE_MYSQL=$(sudo expect -c "

set timeout 10
spawn sudo mysql_secure_installation

expect \"Enter current password for root (enter for none):\"
send \"\r\"

expect \"Change the root password?\"
send \"y\r\"

expect \"New password:?\"
send \"ConSecurMariaDB\r\"

expect \"Re-enter new password:\"
send \"ConSecurMariaDB\r\"

expect \"Remove anonymous users?\"
send \"y\r\"

expect \"Disallow root login remotely?\"
send \"y\r\"

expect \"Remove test database and access to it?\"
send \"y\r\"

expect \"Reload privilege tables now?\"
send \"y\r\"

expect eof
")

sudo echo "$SECURE_MYSQL"

sudo mysql -e "grant all on *.* to root2@localhost identified by 'ConSecurMariaDB' with grant option;"