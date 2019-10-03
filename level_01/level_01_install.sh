#!/bin/bash

#Set location and permission
sudo cp passwords.txt /usr/share/dict/
sudo chown ctf1 /usr/share/dict/passwords.txt
sudo chmod 400 /usr/share/dict/passwords.txt