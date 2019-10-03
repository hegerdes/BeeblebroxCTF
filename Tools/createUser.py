#!/usr/bin/python3
import os
import json
import tools
from subprocess import Popen, PIPE, call

credentials = dict()

def init():
	return(load_credentials())


#Load user ccredentials form txt in script
def load_credentials():
    f = open('../Info/credentials.txt', 'r')
    for line in f:
        tmp1, tmp2 = line.split()
        credentials[tmp1] = tmp2
    
    return(True)

#Print the credentials
def print_credentials():
    for x, y in credentials.items():
        print(x, y)

#write credentials as json
def write_credentials_json():
    with open('../Info/credentials.json', 'w') as json_file:
        json.dump(credentials, json_file)

#Create user acounts, set thair password and change bash
def create_user():
	for x, y in credentials.items():
		print('Setting user: ' + x)
		user_add = 'sudo useradd -m ' + x
		shell_edit = 'sudo chsh -s /bin/bash ' + x
		set_pw = 'sudo echo ' + x + ':' + y + ' | chpasswd'
		add_group = 'sudo usermod -a -G wireshark ' + x
		edit_bashrc1 = 'echo "\n#Clear history every login\nhistory -c" | tee -a /home/' + x + '/.bashrc'
		edit_bashrc2 = 'echo "\n#Set ssh alias for X11 forwarding\nalias ssh=\'ssh -X\'" | tee -a /home/' + x + '/.bashrc'
		edit_bashrc3 = 'echo "\n#Set postman alias \nalias postman=\'/home/ctf/Postman/Postman\'" | tee -a /home/' + x + '/.bashrc'

		ps = Popen([user_add], stdout=PIPE, stderr=PIPE, shell=True)
		if(not tools.check_output(ps)):
			return(False)
		ps = Popen([shell_edit], stdout=PIPE, stderr=PIPE, shell=True)
		if(not tools.check_output(ps)):
			return(False)
		ps = Popen([set_pw], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		if(not tools.check_output(ps)):
			return(False)		
		ps = Popen([add_group], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		if(not tools.check_output(ps)):
			return(False)
		ps = Popen([edit_bashrc1], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		if(not tools.check_output(ps)):
			return(False)
		ps = Popen([edit_bashrc2], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		if(not tools.check_output(ps)):
			return(False)
		ps = Popen([edit_bashrc3], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		if(not tools.check_output(ps)):
			return(False)
	return(True)

#removes all users
def delet_user():
	for x, y in credentials.items():
		userdel = 'sudo userdel ' + x
		rmuserdir = 'sudo rm /home/' + x + ' -rf'
		ps = Popen([userdel], stdout=PIPE, stderr=PIPE, shell=True)
		tools.check_output(ps)
		ps = Popen([rmuserdir], stdout=PIPE, stderr=PIPE, shell=True)
		tools.check_output(ps)
	return(True)

if __name__ == "__main__":
	tools.checkSudo()
	tools.chechandsetCWD()
	init()
	delet_user()
	create_user()

