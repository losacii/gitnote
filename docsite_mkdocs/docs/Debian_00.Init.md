# Debian(0) Initialization

### Download debian 
from [here](https://cdimage.debian.org/debian-cd/10.1.0-live/amd64/iso-hybrid/) standard iso <br>
virutlbox > new > Debian10 <br>
2048 > 25.48G <br>
System > uncheck flopy <br>
Display > 32M <br>
Storage > Select ISO <br>
Network > Bridged Adapter <br>
US Estern

### sudoer add user
(root login)  
vi /etc/suders  
( copy root-line,  
  rename with userName,  
  :wq )  

### Debian Wifi
https://blog.csdn.net/java211/article/details/5053788
    1.查看网卡型号：  
    lsmod | grep iw  
    安装网卡驱动和无线网络配置工具：  
    sudo apt-get install firmware-iwlwifi wireless-tools  
    加载无线网卡驱动：  
    modprobe iwl4965  
    重启系统：    
    reboot  
    此时，网卡应该被探测到！  
    2.查看网卡信息：  
    iwconfig  
    无线网卡一般是wlan0  
    ifconfig wlan0 up #启用无线网卡  
    查看附近可用的无线接入点（AP）  
    iwlist wlan0 scan  
    让无线网卡接入无线网络：  
    iwconfig wlan0 ESSID "linkname" KEY "password" open  

### Update, Remote SSH login
sudo apt update (wait 10 minutes)  

sudo apt install openssh-server  
sudo systemctl enable ssh  
sudo systemctl start ssh  

ip a | grep 192  
( now you can login this machine with: ssh name@ip )  

### sources.list
cd /etc/apt/  
sudo cp sources.list sources.list.bak

vi soures.list  
(Paste [this script](./sourcelist.html) in it)

(paste in, save)  
sudo apt update  

### Neovim & Spacevim
sudo apt-get install make cmake curl ninja-build gettext libtool libtool-bin autoconf automake g++ pkg-config unzip git-core  

sudo apt install python-pip python3-pip  

sudo pip3 install pynvim neovim  

sudo apt install neovim  

(SpaceVim)  
(https://github.com/SpaceVim/SpaceVim)  

curl -sLf https://spacevim.org/install.sh | bash -s -- -h  
sudo curl -sLf https://spacevim.org/install.sh | bash -s -- --install neovim  

## rsync
sudo apt intall rsync  
> rsync -zarP userName@ip:~/documents/ /home/username/documents/  
rsync -zarmv --include-from inlist --exclude="*" $from $to  

