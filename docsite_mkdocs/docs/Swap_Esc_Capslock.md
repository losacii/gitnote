# Swap Escape with Capslock
A solution that should work for most linux distros:  

	setxkbmap -option caps:swapescape  

Other options are possible:  

	caps:none 	to deactivate  
	caps:escape 	to make it an additional escape  
	caps:super 	to make it an additional super (windows) key.  

------------ or ------------------  
sudo apt install console-data  

sudo -i  

cd /usr/share/kbd/keymaps/i386/qwerty/  

cp  us.map.gz  us-nocaps.map.gz  

gunzip us-nocaps.map.gz  

nvim us-nocaps.map  (find 58, you know what to do: 1 --> 58  58 --> 1)  

gzip us-nocaps.map  

loadkeys /usr/share/kbd/keymaps/i386/qwerty/us-nocaps.map.gz  

echo -e "loadkeys /usr/share/kbd/keymaps/i386/qwerty/us-nocaps.map.gz" >> /etc/profile.d/swap_ESC_Capslock.sh  


------------ or ------------------  
sudo -i  
cat >> /etc/default/keyboard  
XKBOPTIONS="caps:swapescape"  
