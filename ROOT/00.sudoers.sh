echo  "losacii ALL=(ALL:ALL) ALL" >> /etc/sudoers
echo  "losacii ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
echo  "usr1    ALL=(ALL:ALL) ALL" >> /etc/sudoers
echo  "vi    ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

ssh-keygen -R 192.168.20.2
ssh-copy-id vi@192.168.20.2


