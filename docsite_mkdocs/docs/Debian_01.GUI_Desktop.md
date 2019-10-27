# Debian(1) GUI Desktop

### locale
vi /etc/default/locale  
>
LANG="en_US.UTF-8"  
LANGUAGE="en_US:en"  

### Generate Locale
```
vim /etc/locale.gen  
```

uncomment this line  
en_US.UTF-8 UTF-8  

```
locale-gen
```

### xorg i3 compton
\- sudo apt install aptitude  
\- sudo apt install xorg  
\- sudo apt install i3  
\- sudo apt install compton compton-conf  
( set active window opacity 0.9, others lower )  
  ( kill process with: **killall -9 compton** )  
\- echo "setxkbmap -option caps:swapescape" > ~/xinitrc  
\- echo "exec i3" > ~/xinitrc  
\-  ( startx )  

### Apps
	- vlc  
  - firefox-esr
  - pcmanfm

### Config Files
  ln ~/.bashrc _bashrc  
  ln ~/.bash_aliases _bash_aliases  
  ln ~/.SpaceVim/config/main.vim _spacevim_main.vim  
  ln ~/.SpaceVim.d/init.toml _spacevim_FVD  
  ln ~/.config/i3/config _i3config  
  ln ~/.xinitrc _xinitrc  

# ~/.cache/vimfiles/repos/github.com/Shougo/neosnippet-snippets/neosnippets


ln ~/.inputrc _inputrc

### i3wm
- https://linoxide.com/gui/install-i3-window-manager-linux/


### vim ~/.config/i3/config
  bindsym $mod+q kill  
  bindsym $mod+d dmenu_run  
  bindsym $mod+t layout toggle split  

  (Focus Window, Move Window)  
  $mod+h  $mod+Shift+h  
  $mod+j  $mod+Shift+j  
  $mod+k  $mod+Shift+k  
  $mod+l  $mod+Shift+l  

### Sound
  sudo apt install alsa-utils
  sudo alsactl init
  alsamixer

  check this url [>>](https://askubuntu.com/questions/454955/using-amixer-to-control-volume)  
  amixer -c 1 Master +10  
  amixer -D pulse sset Master 0%   
  amixer -D pulse sset Master 5%+  
  amixer -D pulse sset Master 0%-  

### Config Files
  ~/.bashrc [script](./configFiles/_bashrc.txt)  
  ~/.bash_aliases [script](./configFiles/_bash_aliases.txt)
  ~/.profile [script](./configFiles/_profile.txt)  
  ~/.xinitrc [script](./configFiles/_xinitrc.txt)  
  ~/.config/i3/config [script](./configFiles/i3_config)  
  ~/.SpaceVim/main.vim [script](./configFiles/Spacevim_main.txt)  
  ~/.SpaceVim.d/init.toml [script](./configFiles/Spacevim_FVD.txt)  

### nnn file manager
  [A blazing Fast Terminal File manager >>>](https://itsfoss.com/nnn-file-browser-linux/)  
  sudo apt install nnn  
  man nnn

  h j k l gg G  

  l  openfile  
  e  edit file  

  <space>  mark it
  V        move to here
  p        paste here
  X        Delete

  Y<move>Y  multiple select
  y    show selected


### fzf
  sudo apt install fzf  

  git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf  
  ~/.fzf/install  


### mkdocs & mkdocs-material & screen
sudo apt install mkdocs screen
pip3 install mkdocs mkdocs-material  

### screenkey & vokoscreen
sudo apt install screenkey  
screenkey --show-settings  
Toggle with:  Left-Ctrl + Right_Ctrl  

vokoscreen 3 hotkeys:  
- **Start**: Ctrl + Shift + F10  
- **Stop**:  Ctrl + Shift + F11  
- **Pause**: Ctrl + Shift + F12  

### VNC Viewer | Nomachine ?
[Download Nomachine Here >>>](https://www.nomachine.com/download)  


### figlet & lolcat
install figlet lolcat  

figlet -f slant "hello"  

lolcat -h  

echo "Alex" | lolcat -a -d 99  

cd /usr/share  
sudo git clone https://github.com/xero/figlet-fonts.git  

mv figlet-fonts/* figlet && rm -rf figlet-fonts  

figlet -f Bloody "C O D" | lolcat -a -d 1  

echo "Alex Alexander" | lolcat -a -d 50 -S 20 -s 30 -p 7  

## tty-clock

sudo apt install tty-clock  
tty-clock --help  
tty-clock -s -x -c  

### openshot - the video editor
sudo apt install -y openshot  

