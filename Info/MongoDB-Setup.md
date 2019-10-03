# Setup MongoDB

This was designed for MongoDB 3.4

## Setup Users

Type: 

```bash
mongod
```

In a new terminal start:

```bash
mongo
#Switch database
use admin
#Create new admin-user
db.createUser({user: "useradmin", pwd: "ConSecurMongoDB",roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] })
#Exit mongo with
crt-D
```

Stop mongod process. And start it again with --auth

```bash
mongod --auth
```

In a new terminal start mongo again:

```bash
mongo
db.auth("useradmin", "ConSecurMongoDB")
#Switch database
use ctf
#Create new user
db.createUser({user: "ctf", pwd: "ConSecurMongoDB",roles: [ { role: "readWrite", db: "ctf" } ] })
#Exit mongo with
crt-D
```

## Make MongoDB start at boot

Create service:

```bash
sudo nano /etc/systemd/system/mymongodb.service
#Past the following
Description=This is my service to start MongoDB

Wants=network.target
After=syslog.target network-online.target

[Service]
Type=simple
ExecStart=sudo mongod --auth
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target
#Save it with crt-o Enter and exit with crt-x
#Run
sudo systemctl daemon-reload
sudo systemctl enable mymongodb
sudo systemctl start mymongodb
sudo systemctl status mymongodb
```
