# Welcome to the ConSecur CTF

This is a training program provided by ConSecur to teach some basic knowledge about remotely managing Linux systems, penetration testing, information gathering and other techniques that an attacker might use to compromise a company's security system.

## 🙌 Motivation and Goal

In this program are some real world techniques that have been used to extract information or harm companies. Some of them are still used. It's important to know these techniques, how your company handles security and how to prevent others to use these techniques to compromise your company.

The goal is to complete all 16 levels of this program. To do so you need to find the password for every level, log into it and find the next password. Every level has its own web page and own user account on this system. The web page gives you information and tips for each level.

## 🎮 How to Play

Congratulation!! If you see this you are probably already logged into the first user account. If not do so. Use the user ctf and password ctf.

To get access to the next level you need to find the password for the next user. The next password is always somehow hidden in your current level. Every password is 32 characters long and only has ASCII characters (so numbers, lower and uppercase letters). To brute forcing it will be quite hard 😝

To find the next password lunch the terminal and start searching. If you found it use ssh to log in to the next user/level. Using the graphical login will not give you any advantages. It will only slow you down and make the training less realistic.

## 🏁 Get stated and don't give up

To make your life easier I installed some extra software like vscode, vim, emacs, sublime-text, build and debug tools, a networksniffer and python3 for scripting. These are some common tools, and they have lots of resources online if you need any help.

Sometimes it's not obviously how to solve the level. If you are stuck don't frustrate. While testing a real world application you will get stuck too. Just rethink your strategy. Inform yourself about the services on the system and their potential weaknesses. If the service expects a 0 give them a 1\. Get a sense of breaking things.

Click [here](task/ctf0) to start with the first level. Good Luck! 👍

# **The Level**

# Level 0

Let's start easy!

The password for the next level is in a file named "-". Just read the password and login to the next level using ssh, the username ctf1, the given IP (or localhost) and the password you just found.

The "ls" command is a good start. This will probably be you're most used command.

## Useful Commands:

Commands you might want to look at:

* ls
* ssh
* cat
* more
* less

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

man is the system's manual viewer; it can be used to display manual pages, scroll up and down, search for occurrences of specific text, and other useful functions. Each argument given to man is normally the name of a program, utility or function. The manual page associated with each of these arguments is then found and displayed.

## Tipp:

* If there is a warning about authentifcation you just need to write yes. * Xauthority warning can be ignored too.
* Spacial filename characters must be escaped.
* Syntax for ssh: ssh [options] user@ip
* To show everything use ls -la.

# Level 1

You need to find the password for level 2.

The password is somewhere on the drive. The file is over 20MB and has lots of other usernames and passwords in it.

To solve this you should use the find command. Look at man find to specify the search. Once the file is found you have to search for ctf2 within the file. Use an text editor or combine terminal tools like "cat" and "grep".

## Useful Commands:

Commands you might want to look at:

* cat
* find
* vim
* nano
* grep

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* The file is owned by ctf1
* The file has ctf2 in it.
* It is called passwords.txt

# Level 2:

Again?

The password file directly in front of you?

Not quite!

Information comes in a variety of forms. Not all are human readable. Some are hidden or encoded so its harder to steal these.

Maybe, but just maybe this is the purpose of this level 🤔

## Useful Commands:

Commands you might want to look at:

* pipes
* hexdump
* strings
* base64
* cat
* file
* xxd

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* The file is in a binary format but cat still can read it.
* The file is in a different encoding base64.
* Use an online converter or the terminal.

# Level 3

Oh, that's kind. The program just gives you the password for the next level. But I think it wants a PIN.

Just play around with the program. There are a several ways to complete this level.

Just to let you know: The PIN is four digits long. You can try all combinations but I would automate this. There are multiple ways to do this. Look at General Tipps for some bash info or klick below.

## Useful Commands:

Commands you might want to look at:

* python
* bash
* nano
* emacs
* vim
* chmod
* ltrace
* gdb

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* Get into bash scripts
* Example: #!/bin/bash echo "Hallo World"
* A for loop might be a good idea
* To call the programm use: ./PW-Safe "-s" "ctf4" $i where i is a number

# Level 4

In this level the password was deleted!

But almost nothing that's deleted is gone forever right? At least not in IT.

Extract the archive and look around this level and figure out how a development team keeps track of who did what and what happens when someone deletes something.

If you are stuck or boared you can just try to start the game. You just need to compile it.

If you need help "man" is you a friend just like google.

## Useful Commands:

Commands you might want to look at:

* ls
* tar
* gzip
* git
* cmake

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* Use ssh -X for grafics forwarding.
* There are several development trees in this reposotory
* Git has lots of other commands and a build in help
* You should try git [log, checkout, show]
* Go back in time/history
* Use make_build.sh for the programm

# Level 5

Seems like someone doesn't want to let you in. Or more like he kicks you out!

How to do something when you are immediately logged off? That's the puzzle for now.

Other than that there is nothing really new. The owner encoded his file to prevent people from using grep to find sensitive information with words like "password" or "ctf".

## Useful Commands:

Commands you might want to look at:

* ssh
* base32
* base64
* xxd

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* Just read manpages of ssh

# Level 6

Something new this time!

There is no need for a black, text only terminal windows this time. Instead you get to open a browser windows and an view "beautiful" website.

To access the level you first have to login as user ctf6 and the associated password Use the top right button for this.

If you logedin click he link below. Now just look around for a little and you will find what you are looking for.

[Klick Here](localhost:8000/ctf/ctf6)

## Useful Commands:

Commands you might want to look at:

* Browser

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* Ever heard of DevTools?
* Like F12

# Level 7

A website again. You will get used to it. There are some more.

Login as ctf7. Then you need to find the password for level 8 but only ctf8 has access to it. This seems impossible.

Or can you trick me to make me think you are ctf8.

[Klick Here](localhost:8000/ctf/ctf7)

## Useful Commands:

Commands you might want to look at:

* Browser

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* Like last time.
* Shhhh! There are some good browser extentions.
* I really like cookies
* What is the opposite of 0 in IT?

# Level 8

Login as ctf8 and click on the link below.

Ohhh! Always these iPhone exclusive apps and websites 🙄

But how does the server know your device?

When you are on an iPhone you better read quick. The site automatically closes after 1 second.

[Klick Here](localhost:8000/ctf/ctf8)

## Useful Commands:

Commands you might want to look at:

* Browser
* Postman
* Browser-Addons

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* How does the server know I'm not on an IPhone
* What is a user-agent?
* To get the page you can also use the terminal or Postman. There is an example on the Tipps site.
* Postman is a GUI tool if you are on a remote system you need a working X-Server or install it on your local pc
* Disable javascript.

# Level 9

I think you have to enter a PIN to get access to the next password.

I know you already cracked a local program with a pin. Now it's the same on the website.

Figure out how to send requests to a web page using a local script. Python might be helpful. You can look at /example2 on this page.

[Klick Here](localhost:8000/ctf/ctf9)

## Useful Commands:

Commands you might want to look at:

* Browser
* Postman
* Python
* Python-reqests
* Python-bs4
* python3-selenium

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* In python use the requests' library.
* To access the page you had to login. So the request also have to authenticate.
* Use cookies = {'Auth': KEY} and append it to your request. Use the data attribute of request and put your numbers in the \"text\" form.

# Level 10

Nice an input form!

I'm supposed to enter a user name.

I don't know about you but I hate it when someone tells me what I'm supposed to do. Always do the opposite.

[Klick Here](localhost:8000/ctf/ctf9)

## Useful Commands:

Commands you might want to look at:

* Browser
* Postman

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* Where are usernames stored?
* This thing, it's called Database.
* And they have there own language.
* Press 12. The relevant table is called Data

# Level 11

Same as last time but harder. Definitely harder. So take your time and stay motivated.

Now the input gets filtered for special characters.

You also don't get direct access to the query result. You only get binary answers. Yes or No. But that's enough to get the password.

[Klick Here](localhost:8000/ctf/ctf11)

## Useful Commands:

Commands you might want to look at:

* Browser
* Postman
* Python
* Python-reqests
* Python-bs4
* python3-selenium

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* Think about SQL injections.
* Combine the last two levels.

# Level 12

There is an executable in your home directory. Start it, give it a port and say hello over the network

You should try a free port with a high number like 8217

## Useful Commands:

Commands you might want to look at:

* nc
* ncat
* namp

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

## Tipp:

* nc the swiss army knife of networking
* I think you should listen

# Level 13

It's time to crack!

Now literary. There is a zip file. You can try to open it but you will not get far.

Luckily "john" will save you.

First you will need to extract the password hash out of the zip files. The tools for this is in the john folder. Next use john to crack the zip.

You have several wordlists. I recommend you to try it without a wordlist and after that witth different wordlists.

## Useful Commands:

Commands you might want to look at:

* john
* zip
* less

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

man is the system's manual viewer; it can be used to display manual pages, scroll up and down, search for occurrences of specific text, and other useful functions. Each argument given to man is normally the name of a program, utility or function. The manual page associated with each of these arguments is then found and displayed.

### Tipp:

To extract it use zip2john

Specify the wordlist with --wordlist=FILE

# Level 14

This time there is no password. Only a picture

Did you ever hear of steganography? It's a technique to hide files in other files. Use "steghide" and see what you find. The password for the extraction is the name of this system

You will see that the file you found is not a password file. In fact it's a key, a ssh-key. 

To use the key you have to change its permission with chmod so that only you can read the file.

## Useful Commands:

Commands you might want to look at:

* stegahide
* ls
* ssh
* chmod

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

man is the system's manual viewer; it can be used to display manual pages, scroll up and down, search for occurrences of specific text, and other useful functions. Each argument given to man is normally the name of a program, utility or function. The manual page associated with each of these arguments is then found and displayed.

### Tipp:

Use man to see the options of "steghide"

Use hostname to find the name of the system

# Level 15

This is very similar to level 12.

But this time you don't have to start the server. It's already running.

But this time you don't know the port the server is running on. Good luck trying all 65535 ports.

It is very important to know the running services and open ports on your system. A way to find them is with nmap. It's one of the best network scanners out there and is used by admins and attackers to find open ports and the services on a system. Now you have to scan this local PC. Then you just connect to the port with nc like in level 12.

## Useful Commands:

Commands you might want to look at:

* nmap
* nc
* ncat

These commands might help you to complete this level. If you don't know how to use them you can look at the manpages.

man is the system's manual viewer; it can be used to display manual pages, scroll up and down, search for occurrences of specific text, and other useful functions. Each argument given to man is normally the name of a program, utility or function. The manual page associated with each of these arguments is then found and displayed.

### Tipp:

nmap has a good man page

Don't just scan the most used ports, scan everything

# WIN

## 🙌 Congratulation!! You did it 🎉

For now, you competed all 15 levels. That's all there is for now.

I really hope you liked this training and had some fun. In the best case, you have also learned something.

I wish you the best for your next tasks and remember: Don't **ever** forget your towel.

## Be proud!

### You now can:

* Safely navigate through Linux
* Manipulate text files
* Write basic bash scripts
* Know how to secure ssl querys
* Know how authentication on the web works
* Know how to scrape the web with python
* Can crack passwords
* Search network for open ports

## Feedback!

Feedback is welcome. You can wrire to:

Stphan Ilic -> ilic@consecur.de (ConSecur)

Henrik Gerdes -> hegerdes@uni-osnabrueck.de (Intern)
