# Setup NodeJS

Setup youd work automatic with packageCheck.py. If not follow these instructions.

NPM musst be installed

## Global forever and nodemon install

Type: 

```bash
npm install nodemon -g
npm install forever -g
```

In a new terminal start:


## Make NodeJS start at boot

Create service:

```bash
sudo nano /etc/systemd/system/nodeserver.service
#Past the following
Description=This is the service for NodeWebserver

Wants=network.target
After=syslog.target network-online.target

[Service]
Type=simple
ExecStart=forever PATH-TO-NODEJSSERVER-APP.JS
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target
#Save it with crt-o Enter and exit with crt-x
#Run
sudo systemctl daemon-reload
sudo systemctl enable nodeserver
sudo systemctl start nodeserver
sudo systemctl status nodeserver
```
