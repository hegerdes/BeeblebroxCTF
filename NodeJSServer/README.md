# WebServer and Web-Level

The WebServer ist powerd by Node.js. It gives some basic tipps and examples for every CTF-Level.  
The levels with the WebServer are desinged in a way that they have vulnerabilities on purpose.

## Prerequisites

Make sure you have these installed on your machine

* [Node.js](https://nodejs.org/en/download/) - The backend framework
* [MongoDB](https://www.mongodb.com) - Non-SQL Database platform
* [npm](https://www.npmjs.com/) - This comes with Node.js, but make sure you check if you have it anyway
* [mariadb](https://mariadb.org/) - SQL Database platform
* A lot of npm packages. Look at the package.json

### Installing packages

Run these commands inside the NodeJSServer folder:

``` bash
npm install
```

### Running the app

``` bash
npm start
```

**Note:** This can be automated by calling:

``` bash
sudo python3 Tools/deployCTF.py
```
