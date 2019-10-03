#!/usr/bin/python3
import shutil
import os
import pymongo
import stat
import time
import tools
from subprocess import Popen, PIPE, call

def setupmongo():
    print('Setting up MongoDB')
    
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["admin"]
    mydb.command("createUser", "useradmin", pwd="ConSecurMongoDB", roles=["userAdminAnyDatabase"])
    myclient.close()
    
    time.sleep(1)

    print('Mongo Admin created. Restarting MongoDB with --auth')
    comand = 'sudo systemctl stop mongod'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    
    comand_path = '/etc/systemd/system/multi-user.target.wants/mongodb.service'

    service = '[Unit]\nDescription=An object/document-oriented database\nDocumentation=man:mongod(1)\nAfter=network.target\n\n[Service]\nUser=mongodb\nGroup=mongodb\nRuntimeDirectory=mongodb\nRuntimeDirectoryMode=0755\nEnvironmentFile=-/etc/default/mongodb\nEnvironment=CONF=/etc/mongodb.conf\nEnvironment=SOCKETPATH=/run/mongodb\nExecStart=/usr/bin/mongod --auth --unixSocketPrefix=${SOCKETPATH} --config ${CONF} $DAEMON_OPTS\nLimitFSIZE=infinity\nLimitCPU=infinity\nLimitAS=infinity\nLimitNOFILE=64000\nLimitNPROC=64000\n\n[Install]\nWantedBy=multi-user.target\n'

    time.sleep(1)
    
    text_file = open(comand_path, 'w')
    text_file.write(service)
    text_file.close()

    print('New daemon written')

    comand = 'sudo systemctl daemon-reload'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    time.sleep(1)
    comand = 'sudo systemctl start mongodb'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    time.sleep(1)
    comand = 'sudo systemctl status mongodb'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

    print('Creating ctf user')
    myclient = pymongo.MongoClient('localhost',username='useradmin',password='ConSecurMongoDB')
    mydb = myclient["ctf"]
    mydb.command("createUser", "ctf", pwd="ConSecurMongoDB", roles=["readWrite"])
    myclient.close()

def setupMongoUsers():
    print('\nRestoring database')
    comand = 'sudo mongorestore -d ctf --uri mongodb://ctf:ConSecurMongoDB@localhost:27017/ctf ../Info/ctf'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

if __name__ == "__main__":
    tools.checkSudo()
    tools.chechandsetCWD()
    setupmongo()
    setupMongoUsers()