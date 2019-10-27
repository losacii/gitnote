sudo useradd -m usr1
sudo passwd usr1
sudo usermod -a -G sudo usr1
sudo chsh -s /bin/bash usr1

su usr1
whoami
echo "cd" >> /home/usr1/.bashrc

## How to add remove user 
## (standard user/non-root)
#
#sudo useradd -m usr1
#sudo passwd usr1
#
## Add user to sudo group 
## (to allow user to install software, allow printing, use privileged mode etc.)
#sudo usermod -a -G sudo usr1
#
## Change default shell of previously created user to bash
#sudo chsh -s /bin/bash usr1
#
#whoami
## :.w !bash


