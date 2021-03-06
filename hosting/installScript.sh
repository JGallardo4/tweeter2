#!/usr/bin/env bash

BLINKGREEN='\033[32;5m';
BLINKEND='\033[0m';
GREEN='\033[0;32m';
RED='\033[0;31m';
YELLOW='\033[0;33m';
WHITE='\033[0;37m';

echo "";
echo -e "${BLINKGREEN}UPDATING${BLINKEND}";
echo "";

sudo apt -y update;
sudo apt -y upgrade;

echo "";
echo -e "${BLINKGREEN}CREATING SWAP MEMORY${BLINKEND}";
echo "";

sudo fallocate -l 5G /swapfile;
sudo chmod 600 /swapfile;
sudo mkswap /swapfile;
sudo swapon /swapfile;
sudo echo "/swapfile swap swap defaults 0 0" >> /etc/fstab;

echo "";
echo -e "${BLINKGREEN}INSTALLING APACHE${BLINKEND}";
echo "";
sudo apt install -y apache2;

echo "";
echo -e "${BLINKGREEN}INSTALLING DATABASE${BLINKEND}";
echo "";
sudo apt install -y mariadb-server;

echo "";
echo -e "${BLINKGREEN}INSTALLING UTILITIES${BLINKEND}";
echo "";
sudo apt-get install -y certbot python-certbot-apache;
sudo apt-get install -y git;
sudo apt-get install -y unzip;
sudo apt-get install -y wget;

echo "";
echo -e "${BLINKGREEN}INSTALLING NODE${BLINKEND}";
echo "";
sudo wget -O $HOME/node.tar.xz https://nodejs.org/dist/v12.16.1/node-v12.16.1-linux-x64.tar.xz;
sudo tar -xJf $HOME/node.tar.xz;
sudo mv $HOME/node-v12.16.1-linux-x64 /node
echo 'export PATH=$PATH:/node/bin' | sudo tee -a ~/.bashrc;
export PATH=$PATH:/node/bin;
sudo chmod 777 /node;

echo "";
echo -e "${BLINKGREEN}INSTALLING PYTHON, THIS WILL TAKE A VERY LONG TIME${BLINKEND}";
echo "";
sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev;
wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz;
tar -xf Python-3.8.2.tar.xz;
cd Python-3.8.2;
sudo ./configure --enable-optimizations --enable-shared;
sudo make;
sudo make altinstall;

cd ..;
rm Python-3.8.2.tar.xz;

echo "";
echo -e "${BLINKGREEN}INSTALLATION FINISHED! PLEASE READ BELOW${BLINKEND}";
echo "";
echo -e "${GREEN}Alex here,";
echo -e "${YELLOW}PLEASE MAKE SURE YOU RUN THE COMMAND ${WHITE}source ~/.bashrc";
echo -e "${GREEN}This will only have to be done once, but it is needed after this script runs"
echo -e "${GREEN}You're all set!";
echo -e "";
echo -e "${WHITE}----------";
echo -e "";
echo -e "${GREEN}You now have a web server up and running, with python, git, and an sql DB installed for you!";
echo -e "${RED}IMPORTANT: ${GREEN}You will have to use GIT to transfer files between the work you do on your editor locally and the work you want to reflect on the server";
echo -e "";
