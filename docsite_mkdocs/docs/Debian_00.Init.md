# Debian(0) Init

### sudoer add user
(root login)  
vi /etc/suders  
( copy root-line,  
  rename with userName,  
  :wq )  

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

pip install pynvim neovim  
pip3 install pynvim neovim  

sudo apt install neovim  

(SpaceVim)  
(https://github.com/SpaceVim/SpaceVim)  

curl -sLf https://spacevim.org/install.sh | bash -s -- -h  
sudo curl -sLf https://spacevim.org/install.sh | bash -s -- --install neovim  

## rsync
sudo apt intall rsync  
> rsync -zarP userName@ip:~/documents/ /home/username/documents/  
rsync -zarmv --include-from inlist --exclude="*" $from $to  

