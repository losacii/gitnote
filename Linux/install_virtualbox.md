# root

vim /etc/apt/source.list.d/virtualbox.list  
(add this line)  
deb https://download.virtualbox.org/virtualbox/debian  buster contrib  

wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | apt-key add -

apt-get update  
apt-get install virtualbox-6.0  
