#!/bin/bash

#Set location and permission
sudo cp Game.tar.gz /home/ctf4
sudo gunzip /home/ctf4/Game.tar.gz
sudo tar xfv /home/ctf4/Game.tar -C /home/ctf4
sudo chown ctf4 /home/ctf4/Game
sudo rm /home/ctf4/Game.tar

