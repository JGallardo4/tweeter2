sudo apt remove -y mariadb-server
sudo apt install -y software-properties-common dirmngr
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xF1656F24C74CD1D8
sudo add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://mirror.zol.co.zw/mariadb/repo/10.4/debian stretch main'
sudo apt update
sudo apt upgrade
sudo apt install -y mariadb-server mariadb-client
