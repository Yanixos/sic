#!/bin/bash

if [[ $EUID -ne 0 ]]; then
  echo "You need to be root to run this program." 2>&1
  exit 1
fi

#sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get -y install python3.6
sudo apt-get update
sudo apt-get -y install python-setuptools
sudo apt-get -y install python3-setuptools
sudo apt-get -y install python-dev 
sudo apt-get -y install python3-dev
sudo apt-get -y install python3-pip
sudo apt-get -y install postgresql libpq-dev postgresql-client postgresql-client-common
sudo apt-get -y install daemontools daemontools-run
sudo easy_install hashlib
clear
sudo pip3 install -r requirements.txt
sudo pip install psycopg2==2.7.3.2
pip install psycopg2==2.7.3.2
sudo pip3 install psycopg2==2.7.3.2
pip3 install psycopg2==2.7.3.2
clear
sudo mkdir /usr/share/sic
clear
sudo cp -r * /usr/share/sic/
sudo echo "alias sic='sudo /usr/share/sic/sic'" >> ~/.bashrc
sudo chmod 700 /usr/share/sic/*.py /usr/share/sic/*.sh /usr/share/sic/AllFiles.list
clear
printf "For security reasons this tool requires a mail for :\n"
printf "\t- Sending scan results\n"
printf "\t- Sending alert when the database is updated\n"
printf "Please, enter your mail :\n"
read mail
echo $mail | base64 | tr 'A-Za-z' 'N-ZA-Mn-za-m' > /usr/share/sic/.email
sudo chmod 400 /usr/share/sic/.email /usr/share/sic/BinFiles.list
printf "Press Enter..."
read
clear
printf "Use this key to update the baseline database : \n"
sudo python3.6 /usr/share/sic/key_gen.py
printf "This key is generated once, keep it safe.\n"
printf "Press Enter..."
read 
clear
sudo -u postgres -s psql -c "CREATE USER sic_user WITH PASSWORD '0xi3zgYpOEgLw' CREATEDB;"
sudo -u postgres -s psql -c "CREATE DATABASE sic_db OWNER sic_user;"
clear
printf "The basaline database will be generated, it will take some time...\n"
printf "Press Enter...\n"
read
sudo cat /var/log/apt/history.log > /usr/share/sic/.sys_update
sudo chmod 400 /usr/share/sic/.sys_update
sudo python3.6 /usr/share/sic/sic init
clear
printf "The baseline database has been generated\n"
printf "Now, you can use sic, check the help page : sic --help\n"
sudo python3.6 emails.py 
printf "Press Enter..."
read
clear

