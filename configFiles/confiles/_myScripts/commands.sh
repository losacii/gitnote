~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
sudo mv /etc/apt/source.list /etc/apt/source.list.back
sudo wget https://raw.githubusercontent.com/losacii/gitnote/master/debsource.txt -O /etc/apt/source.list
sudo apt update
sudo apt upgrade



~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
sudo apt install openssh-server
    sudo systemctl enable ssh
    sudo systemctl start ssh



~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
ssh-keygen -R IP
ssh user@IP





~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
sudo vi /etc/sudoers



~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
sudo apt install git-core
git clone https://github.com/losacii/gitnote.git

.bashrc
  PS1
  source .bash_aliases
  source .myscripts




~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
sudo apt install python-pip python3-pip

pip3 install pqi
.local/bin/pqi use tuna

pip install pynvim neovim

pip3 install pynvim neovim

sudo apt install make cmake curl ninja-build gettext libtool \
  libtool-bin autoconf automake g++ pkg-config unzip




~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
appinstall rsync




~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
sudo nvim /etc/default/locale
	LANG="en_US.UTF-8"
	LANGUAGE="en_US:en"

sudo nvim /etc/locale.gen
	( uncomment this line )
	en_US.UTF-8 UTF-8

sudo locale-gen





~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~




~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
ultisnippets

ncm2 options

lsp kite







