#!/usr/bin/python3
import tools
import packageCheck
import createUser
import setMongoDB
import setMariaDB
import os
import installLevel

if __name__ == "__main__":
    tools.checkSudo()
    tools.chechandsetCWD()

    print('Hello. This Script will try to deploy the Beeblebrox CTF')
    print('Starting with the needed tools')
    
    #Ceck installed tools
    if(not packageCheck.run()):
        print('Unable to install the needed progams. Please install manual.')
        exit(1)

    
     #Ask user if mongodb authentificatiion is set
    while True:
        print('Is MongoDB authentification set? y/n ')
        response = input()
        if(response == 'n'):
            print('Setting up mongodb ctf database')
            setMongoDB.setupmongo()
            break
        if(response == 'y'):
            print('Skip')
            break
        print('Please type y or n or s')

    #Ask user if mongodb content is alrady set
    while True:
        print('Does the MongoDB alrady have a ctf Database and its users? y/n')
        response = input()
        if(response == 'n'):
            print('Setting up mongodb ctf database')
            setMongoDB.setupMongoUsers()
            break
        if(response == 'y'):
            print('Skip mongodb setup')
            break
        print('Please type y or n')

    #Ask user if the custem node-deamon is alrady set
    while True:
        print('Are npm, node-demon and node-modules alrady set? y/n')
        response = input()
        if(response == 'n'):
            print('Setting up npm')
            packageCheck.npm_tools()
            break
        if(response == 'y'):
            print('Skip npm update')
            break
        print('Please type y or n')

     #Ask user if the MariaDB is set up
    while True:
        print('Does the MariaDB alrady have its users and dbs? y/n')
        response = input()
        if(response == 'n'):
            print('Setting up MariaDB')
            setMariaDB.securMaria()
            setMariaDB.createUser()
            setMariaDB.createDB()
            setMariaDB.insertData()
            break
        if(response == 'y'):
            print('Skip MariaDB setup')
            break
        print('Please type y or n')
    
    #Read user-info and create them
    print('\nTry to crate all users:')
    if(not createUser.init()):
        print('Unable to find the UserData')
    while True:
        print('Existing ctf users will be deleted.\nDo the accounts alrady exist? y/n ')
        response = input()
        if(response == 'n'):
            break
        if(response == 'y'):
            print('Removing old users')
            createUser.delet_user()
            break
        print('Please type y or n')
    if(not createUser.create_user()):
        print('Unable to create users. Please fix error or set them up manual.')
        exit(1)
    
    #Install the level
    print('\nCopying files for CTF-Levels..')
    installLevel.installAll()