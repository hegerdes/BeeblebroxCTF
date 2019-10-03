#!/usr/bin/python3
import gzip
import shutil
import pwd
import grp
import os
import time
import urllib.request
import tarfile
import stat
import tools
from subprocess import Popen, PIPE, call

def level0():
    print('Setting up level 0')
    path = '/home/ctf/-'
    gid = grp.getgrnam("ctf").gr_gid
    uid = pwd.getpwnam("ctf").pw_uid
    shutil.copy('../level_00/-', path)


    os.chown(path, uid, gid)
    os.chmod('/home/ctf', 0o700)
    os.chmod(path, 0o400)

    #Setting welcome and autolunch for firefox
    shutil.copy('../Info/Welcome.ascii', '/home/ctf/welcome')
    os.chmod('/home/ctf/welcome', 0o444)
    edit_bashrc = 'echo "cat welcome" | tee -a /home/ctf/.bashrc'
    ps = Popen([edit_bashrc], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    edit_bashrc = 'echo "firefox localhost:8000 &" | tee -a /home/ctf/.bashrc'
    ps = Popen([edit_bashrc], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

def level1():
    print('Setting up level 1')
    path = '/usr/share/dict/passwords.txt'
    gid = grp.getgrnam("ctf1").gr_gid
    uid = pwd.getpwnam("ctf1").pw_uid
    
    shutil.copy('../level_01/passwords.txt', path)
    os.chown(path, uid, gid)
    os.chmod('/home/ctf1', 0o700)
    os.chmod(path, stat.S_IRUSR)

def level2():
    print('Setting up level 2')
    path = '/home/ctf2/pw.bin'
    gid = grp.getgrnam("ctf2").gr_gid
    uid = pwd.getpwnam("ctf2").pw_uid
    
    shutil.copy('../level_02/pw.bin', path)
    os.chown(path, uid, gid)
    os.chmod('/home/ctf2', 0o700)
    os.chmod(path, stat.S_IRUSR)

def level3():
    print('Setting up level 3')
    path = '/home/ctf3/PW-Safe'
    gid = grp.getgrnam("ctf3").gr_gid
    uid = pwd.getpwnam("ctf3").pw_uid
    
    shutil.copy('../level_03/PW-Safe', path)
    os.chown(path, uid, gid)
    os.chmod('/home/ctf3', 0o700)
    os.chmod(path, stat.S_IRWXU)

def level4():
    print('Setting up level 4')
    path = '/home/ctf4/Game.tar.gz'
    gid = grp.getgrnam("ctf4").gr_gid
    uid = pwd.getpwnam("ctf4").pw_uid
    
    shutil.copy('../level_04/Game.tar.gz', path)

    os.chown('/home/ctf4/Game.tar.gz', uid, gid)
    os.chmod('/home/ctf4', 0o700)
    os.chmod('/home/ctf4/Game.tar.gz', stat.S_IRWXU)

def level5():
    print('Setting up level 5')
    path = '/home/ctf5/ReadMe'
    gid = grp.getgrnam("ctf5").gr_gid
    uid = pwd.getpwnam("ctf5").pw_uid
    
    shutil.copy('../level_05/ReadMe', path)
    os.chown(path, uid, gid)
    os.chmod('/home/ctf5', 0o700)
    os.chmod(path, stat.S_IRUSR)

    edit_bashrc = 'echo "exit" | tee -a /home/ctf5/.bashrc'
    ps = Popen([edit_bashrc], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

def level6():
    print('Setting up level 6')
    path = '/home/ctf6/Level6.md'
    gid = grp.getgrnam("ctf6").gr_gid
    uid = pwd.getpwnam("ctf6").pw_uid
    
    shutil.copy('../level_06/Level6.md', path)

    os.chown(path, uid, gid)
    os.chmod('/home/ctf6', 0o700)

def level7():
    print('Setting up level 7')
    path = '/home/ctf7/Level7.md'
    gid = grp.getgrnam("ctf7").gr_gid
    uid = pwd.getpwnam("ctf7").pw_uid
    
    shutil.copy('../level_07/Level7.md', path)

    os.chown(path, uid, gid)
    os.chmod('/home/ctf7', 0o700)

def level8():
    print('Setting up level 8')
    path = '/home/ctf8/Level8.md'
    gid = grp.getgrnam("ctf8").gr_gid
    uid = pwd.getpwnam("ctf8").pw_uid
    
    shutil.copy('../level_08/Level8.md', path)

    os.chown(path, uid, gid)
    os.chmod('/home/ctf8', 0o700)

def level9():
    print('Setting up level 9')
    path = '/home/ctf9/Level9.md'
    gid = grp.getgrnam("ctf9").gr_gid
    uid = pwd.getpwnam("ctf9").pw_uid
    
    shutil.copy('../level_09/Level9.md', path)

    os.chown(path, uid, gid)
    os.chmod('/home/ctf9', 0o700)

def level10():
    print('Setting up level 10')
    path = '/home/ctf10/Level10.md'
    gid = grp.getgrnam("ctf10").gr_gid
    uid = pwd.getpwnam("ctf10").pw_uid
    
    shutil.copy('../level_10/Level10.md', path)

    os.chown(path, uid, gid)
    os.chmod('/home/ctf10', 0o700)

def level11():
    print('Setting up level 11')
    path = '/home/ctf11/Level11.md'
    gid = grp.getgrnam("ctf11").gr_gid
    uid = pwd.getpwnam("ctf11").pw_uid
    
    shutil.copy('../level_11/Level11.md', path)

    os.chown(path, uid, gid)
    
    os.chmod('/home/ctf11', 0o700)

def level12():
    print('Setting up level 12')
    gid = grp.getgrnam("ctf12").gr_gid
    uid = pwd.getpwnam("ctf12").pw_uid
    
    shutil.copy('../level_12/Server', '/home/ctf12/Server')
    shutil.copy('../level_12/ReadMe.md', '/home/ctf12/ReadMe.md')

    os.chown('/home/ctf12/ReadMe.md', uid, gid)
    os.chmod('/home/ctf12/ReadMe.md', 0o500)

    os.chown('/home/ctf12/Server', uid, gid)
    os.chmod('/home/ctf12/Server', 0o500)

    os.chmod('/home/ctf12', 0o700)

def level13():
    print('Setting up level 13')
    gid = grp.getgrnam("ctf13").gr_gid
    uid = pwd.getpwnam("ctf13").pw_uid
    
    shutil.copy('../level_13/john.tar.gz', '/home/ctf13/john.tar.gz')
    shutil.copy('../level_13/pw.zip', '/home/ctf13/pw.zip')

    os.chown('/home/ctf13/pw.zip', uid, gid)
    os.chmod('/home/ctf13/pw.zip', 0o700)

    tar = tarfile.open('/home/ctf13/john.tar.gz', "r:gz")
    tar.extractall(path='/home/ctf13/')
    tar.close()
    
    os.rename('/home/ctf13/run', '/home/ctf13/john')
    
    tar = tarfile.open('../Info/data/PWLists.tar.gz', "r:gz")
    tar.extractall(path='/home/ctf13/wordlists')
    tar.close()
    
    os.chown('/home/ctf13/john', uid, gid)
    os.chmod('/home/ctf13/john', 0o700)
    
    owner_edit = 'sudo chown -R ctf13 /home/ctf13/john'
    ps = Popen([owner_edit], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

    owner_edit = 'sudo chown -R ctf13 /home/ctf13/wordlists'
    ps = Popen([owner_edit], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)


    os.remove('/home/ctf13/john.tar.gz')

    os.chmod('/home/ctf13', 0o700)

def level14():
    print('Setting up level 14')
    gid = grp.getgrnam("ctf14").gr_gid
    uid = pwd.getpwnam("ctf14").pw_uid
    
    shutil.copy('../level_14/hack_this.jpg', '/home/ctf14/hack_this.jpg')
    
    os.chown('/home/ctf14/hack_this.jpg', uid, gid)
    os.chmod('/home/ctf14/hack_this.jpg', 0o700)

    ssh_login = 'sshpass -p 6E8Wmjx7DjkVixD4whK9NRNnUsfHY98p ssh -t -o StrictHostKeyChecking=no ctf15@localhost "exit"' 
    ps = Popen([ssh_login], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

    set_ssh = 'sudo sshpass -p 6E8Wmjx7DjkVixD4whK9NRNnUsfHY98p ssh-copy-id -i ../level_14/tatu-key-ecdsa ctf15@localhost'
    ps = Popen([set_ssh], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

    os.chown('/home/ctf14/hack_this.jpg', uid, gid)
    os.chmod('/home/ctf14/hack_this.jpg', 0o700)

    os.chmod('/home/ctf14', 0o700)

def level15():
    print('Setting up level 15')

    #For last level
    gid = grp.getgrnam("ctf15").gr_gid
    uid = pwd.getpwnam("ctf15").pw_uid
    
    shutil.copy('../level_15/ctf15.pw', '/home/ctf15/ctf15.pw')
    shutil.copy('../level_15/ReadMe.md', '/home/ctf15/ReadMe.md')
    shutil.copy('../level_15/Server', '/home/ctf15/Server')
    
    os.chown('/home/ctf15/ctf15.pw', uid, gid)
    os.chmod('/home/ctf15/ctf15.pw', 0o400)

    os.chown('/home/ctf15/ReadMe.md', uid, gid)
    os.chmod('/home/ctf15/ReadMe.md', 0o400)

    os.chown('/home/ctf15/Server', uid, gid)
    os.chmod('/home/ctf15/Server', 0o400)

    #For current level
    dir_path = os.path.dirname(os.path.realpath(__file__))
    servercommand = '' + dir_path[:-5] + 'Info/data/Server'

    comand_path = '/etc/systemd/system/ctfserver.service'

    service = 'Description=This starts the socket on prot 4242 that the user has to find\n\nWants=network.target\nAfter=syslog.target network-online.target\n\n[Service]\nType=simple\nExecStart=' + servercommand +'\nRestart=on-failure\nRestartSec=10\nKillMode=process\n\n[Install]\nWantedBy=multi-user.target'

    text_file = open(comand_path, 'w')
    text_file.write(service)
    text_file.close()

    comand = 'sudo systemctl daemon-reload'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    comand = 'sudo systemctl enable ctfserver'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    comand = 'sudo systemctl start ctfserver'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)
    comand = 'sudo systemctl status ctfserver'
    ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

    #Aternative: Start programm with ./bashrc
	# add_serverstart = 'echo "\n#Clear history every login\n/SERVER &" | tee -a /home/' + x + '/.bashrc'
    # ps = Popen([comand], stdout=PIPE, stderr=PIPE, shell=True)
    # tools.check_output(ps)


    os.chmod('/home/ctf15', 0o700)

def level16():
    print('Setting up level 16')
    gid = grp.getgrnam("ctf16").gr_gid
    uid = pwd.getpwnam("ctf16").pw_uid
    
    shutil.copy('../level_16/win.md', '/home/ctf16/win.md')

    os.chown('/home/ctf16/win.md', uid, gid)
    os.chmod('/home/ctf16/win.md', 0o500)

    os.chmod('/home/ctf15', 0o700)

def downloadPostman():
    print('Downloading ...')
    url = 'https://dl.pstmn.io/download/latest/linux64'
    urllib.request.urlretrieve(url, 'Downloads/postman.tar.gz')

def postman():
    print('Setting up Postman')
    downloadPostman()
    print('Installing ...')

    path = 'Downloads/postman.tar.gz'
    gid = grp.getgrnam("ctf").gr_gid
    uid = pwd.getpwnam("ctf").pw_uid
    
    shutil.copy('Downloads/postman.tar.gz', '/home/ctf/')

    tar = tarfile.open(path, "r:gz")
    tar.extractall(path='/home/ctf/')
    tar.close()

    os.chown('/home/ctf/Postman', uid, gid)
    os.chmod('/home/ctf/Postman', 0o777)
    os.remove(path)

def welcomeMSG():
    shutil.copy('../Info/Welcome.ascii', '/etc/motd')

def securInstall():
    print('Securing the install')
    gid = os.getegid()
    uid = os.geteuid()

    os.chmod(os.environ['HOME'], 0o700)

    pash = os.environ['HOME']

    per_edit = 'sudo chmod -R 700 ' + pash
    ps = Popen([per_edit], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

    dir_path = os.path.dirname(os.path.realpath(__file__))

    per_edit = 'sudo chmod -R 700 ' + dir_path
    ps = Popen([per_edit], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)


def sshX11():
    ssh_edit = 'echo "    ForwardX11 yes" | tee -a /etc/ssh/ssh_config'
    ps = Popen([ssh_edit], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

def alterhosts():
    hosts_edit = 'echo "127.0.0.1       BeeblebroxCTF.com" | tee -a /etc/hosts'
    ps = Popen([hosts_edit], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    tools.check_output(ps)

def cron():
    gid = grp.getgrnam("root").gr_gid
    uid = pwd.getpwnam("root").pw_uid
    
    shutil.copy('../Info/data/root', '/var/spool/cron/root')

    os.chown('/var/spool/cron/root', uid, gid)
    os.chmod('/var/spool/cron/root', 0o600)

def removeCred():
    os.remove('../Info/credentials.txt')
    os.remove('../Info/credentials.json')

def postInstall():
    print('\nPostInstall...')
    sshX11()
    postman()
    welcomeMSG()
    securInstall()
    removeCred()

    

def installAll():
    level0()
    level1()
    level2()
    level3()
    level4()
    level5()
    level6()
    level7()
    level8()
    level9()
    level10()
    level11()
    level12()
    level13()
    level14()
    level15()
    postInstall()


if __name__ == "__main__":
    tools.checkSudo()
    tools.chechandsetCWD()
    installAll()
    # cron()