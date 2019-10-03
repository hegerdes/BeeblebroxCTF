#!/usr/bin/python3
import apt
import sys
import os
import time
import tools
import urllib.request
from subprocess import Popen, PIPE, call

#Following packages must be installed:
needed_packets = ['openssh-server', 'git', 'openssh-client', 'tmux', 'chromium', 'python3', 'python3-pip', 'nodejs', 'npm', 'vim', 'curl', 
    'wget', 'libglew-dev', 'libgl1-mesa-dev', 'libjpeg-dev', 'libboost-all-dev', 'xxd', 'xclip', 'fonts-noto-color-emoji', 'mongodb','htop',
    'wireshark', 'xbase-clients', 'python3-pymongo', 'python3-bs4', 'python3-urllib3', 'emacs', 'python3-mysqldb', 'python3-selenium', 'mariadb-server',
    'expect', 'chromium-driver', 'tcpdump', 'zip', 'ncat', 'ltrace', 'cmake', 'sshpass', 'nmap', 'steghide']

    #'libsdl2-dev',

def file_exists(fname):
    try:
        os.stat(fname)
        return True
    except OSError:
        return False


def checkInstall(packetlist):
    cache = apt.Cache()

    not_installed = []

    print('Checking installed packets:\n')
    for x in packetlist:
        if cache[x].is_installed:
            print('Checking: ' + x + ' ✓ ')
        else:
            not_installed.append(x)
    return not_installed

def installpackets(packetlist):
    cache = apt.Cache()

    failed_install = []

    print('\nThe following packets are not installed but needed:')
    for x in packetlist:
        if(x == 'wireshark'): print('You have to allow non admins to capture packets')
        print('Try to install ' + x + '\n') 
        cache[x].mark_install()
        try:
            cache.commit()
            time.sleep(3)
        except:
            failed_install.append(x)
            print(sys.stderr)

    if (len(failed_install) != 0):
        print('unable to install the following packets. Plese install manuel\n')
        print(failed_install)
        return(False)
    return(True)

def installPips():
    comand = 'sudo pip3 install mysql-connector'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

def npm_tools():
    print('\nUpdating and installing npm tools ...')

    comand = 'sudo npm install -g npm@latest'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    comand = 'sudo npm install nodemon -g'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    comand = 'sudo npm install forever -g'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    comand = 'npm install --prefix ../NodeJSServer'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    
    print('Try to set demon for NodeServer...')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    nodecommand = 'forever ' + dir_path[:-5] + 'NodeJSServer/app.js'
    comand_path = '/etc/systemd/system/nodeserver.service'

    service = 'Description=This starts the NodeJS Webserver\n\nWants=network.target\nAfter=syslog.target network-online.target\n\n[Service]\nType=simple\nExecStart=' + nodecommand +'\nRestart=on-failure\nRestartSec=10\nKillMode=process\n\n[Install]\nWantedBy=multi-user.target'

    text_file = open(comand_path, 'w')
    text_file.write(service)
    text_file.close()

    comand = 'sudo systemctl daemon-reload'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    comand = 'sudo systemctl enable nodeserver'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    comand = 'sudo systemctl start nodeserver'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    comand = 'sudo systemctl status nodeserver'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

def setScripts():
    comand = 'sudo cat ../Info/Welcome.ascii | sudo tee /etc/motd'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    

def run():
    if file_exists('/usr/bin/zypper'):
        print('Sorry SUSE ist not supported right now')
        return(False)
    elif file_exists('/usr/bin/apt-get'):
        status = True
        not_installed = checkInstall(needed_packets)
        if(len(not_installed) > 0):
            status = (installpackets(not_installed))
        return(status)
    elif file_exists('/usr/bin/yum'):
        print('Sorry Radhad ist not supported right now')
        return(False)
    else:
        print('cannot find a usable package manager')
        return(False)

if __name__ == "__main__":
    tools.checkSudo()
    tools.chechandsetCWD()
    run()
    installPips()
    npm_tools()
    setScripts()