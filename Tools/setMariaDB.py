import mysql.connector as mariadb
import os
import tools
import time
from subprocess import Popen, PIPE, call

def securMaria():
    print('Securing the MariaDB install...')
    command = 'sudo ./secureMaria.sh'
    ps = Popen([command], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps,True)
    time.sleep(11)

def createUser():
    print('Adding additional users...')
    mariadb_connection = mariadb.connect(user='root2', password='ConSecurMariaDB')
    cursor = mariadb_connection.cursor()

    cursor.execute("CREATE USER ctf10@'%' IDENTIFIED BY 'ConSecurMariaDB'")
    mariadb_connection.commit()
    cursor.execute("GRANT SELECT ON ctf10.* TO ctf10@'%'")
    mariadb_connection.commit()

    cursor.execute("CREATE USER ctf11@'%' IDENTIFIED BY 'ConSecurMariaDB'")
    mariadb_connection.commit()
    cursor.execute("GRANT SELECT ON ctf11.* TO ctf11@'%'")
    mariadb_connection.commit()

def createDB():
    print('Filling the DB...')
    mariadb_connection = mariadb.connect(user='root2', password='ConSecurMariaDB')
    cursor = mariadb_connection.cursor()

    cursor.execute("CREATE DATABASE ctf10")
    mariadb_connection.commit()
    cursor.execute("CREATE DATABASE ctf11")
    mariadb_connection.commit()


    cursor.execute("CREATE TABLE ctf10.Data (user varchar(100) NOT NULL, pw varchar(100) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci")
    mariadb_connection.commit()

    cursor.execute("CREATE TABLE ctf11.Data (user varchar(100) NOT NULL, pw varchar(100) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci")
    mariadb_connection.commit()
    


def insertData10():
    mariadb_connection = mariadb.connect(user='root2', password='ConSecurMariaDB', database='ctf10')
    cursor = mariadb_connection.cursor()

    f = open('../Info/DB/UserPW10.txt', 'r')
    for line in f:
        user, pw = line.split(';')
        pw = pw.rstrip()
        cursor.execute("INSERT INTO Data (user,pw) VALUES (%s,%s)", (user, pw))
        mariadb_connection.commit()

def insertData11():
    mariadb_connection = mariadb.connect(user='root2', password='ConSecurMariaDB', database='ctf11')
    cursor = mariadb_connection.cursor()

    f = open('../Info/DB/UserPW11.txt', 'r')
    for line in f:
        user, pw = line.split(';')
        pw = pw.rstrip()
        cursor.execute("INSERT INTO Data (user,pw) VALUES (%s,%s)", (user, pw))
        mariadb_connection.commit()

def insertData():
    insertData10()
    insertData11()


    


if __name__ == "__main__":
    tools.checkSudo()
    tools.chechandsetCWD()
    # securMaria()
    createUser()
    createDB()
    insertData()