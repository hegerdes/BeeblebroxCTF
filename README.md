# This is a CTF I desinged within an internship

## About this ctf

### Welcome to the Beeblebrox CTF

This is a training program provided by Beeblebrox to teach some basic knowledge about remotely managing Linux systems, penetration testing, information gathering and other techniques that an attacker might use to compromise a company's security system.

### 🙌 Motivation and Goal

In this program are some real world techniques that have been used to extract information or harm companies. Some of them are still used. It's important to know these techniques, how your company handles security and how to prevent others to use these techniques to compromise your company.

The goal is to complete all 16 levels of this program. To do so you need to find the password for every level, log into it and find the next password. Every level has its own web page and own user account on this system. The web page gives you information and tips for each level.

### 🎮 How to Play

Congratulation!! If you see this you are probably already logged into the first user account. If not do so. Use the user ctf and password ctf.

To get access to the next level you need to find the password for the next user. The next password is always somehow hidden in your current level. Every password is 32 characters long and only has ASCII characters (so numbers, lower and uppercase letters). To brute forcing it will be quite hard 😝

To find the next password lunch the terminal and start searching. If you found it use ssh to log in to the next user/level. Using the graphical login will not give you any advantages. It will only slow you down and make the training less realistic.

### 🏁 Get stated and don't give up

To make your life easier I installed some extra software like vscode, vim, emacs, sublime-text, build and debug tools, a networksniffer and python3 for scripting. These are some common tools, and they have lots of resources online if you need any help.

Sometimes it's not obviously how to solve the level. If you are stuck don't frustrate. While testing a real world application you will get stuck too. Just rethink your strategy. Inform yourself about the services on the system and their potential weaknesses. If the service expects a 0 give them a 1\. Get a sense of breaking things.
More information will follow.

## Install

You can install/deploy this ctf yourself but this is not recomended there is a compressed VirtualBox image. If you still want to try deply it yourself sse the Tools/deploy.py scrpt. *NOTE* The script was only created for easier development and not for others to use. So there is no support for this.
