# Setup MariaDB

This is a manual guide to set up MariaDB for this ctf

## SecureMaria

Secure the install. Default root pw is empty. Set the pw to ConSecurMariaDB.

```bash
mysql_secure_installation
ENTER
y
ConSecurMariaDB
ConSecurMariaDB
y
y
y
y
```

## Create users

```bash
mysql -u root -p

#Create database
CREATE DATABASE 'ctf9';
CREATE DATABASE 'ctf10';

#Create user
CREATE USER 'ctf9'@'%' IDENTIFIED BY 'ConSecurMariaDB';
GRANT SELECT ON ctf9.* TO 'ctf9'@'%';

CREATE USER 'ctf10'@'%' IDENTIFIED BY 'ConSecurMariaDB';
GRANT SELECT ON ctf10.* TO 'ctf10'@'%';

```

## Fill the DB

You can import the Database or fill it yourself:

### Import

```bash
mysql -u [user] -p --all-databases < DB/all_databases.sql
```

### Fill it yourself

For every DB create a table named Data

```bash
mysql -u root -p

CREATE TABLE ctf9.Data (' user' varchar(100) NOT NULL, pw varchar(100) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
CREATE TABLE ctf10.Data ( 'user' varchar(100) NOT NULL, pw varchar(100) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
for line in DB/UserPW09 do
    INSERT INTO ctf9.Data (user,pw) VALUES (USERNAME,PW)
done

for line in DB/UserPW10 do
    INSERT INTO ctf10.Data (user,pw) VALUES (USERNAME,PW)
done

```
