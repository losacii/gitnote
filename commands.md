## setting files Linking
    ln ROOT/mysettings/files/_vimrc.for.vimplug ~/.config/nvim/init.vim

## nmap network scanning
    sudo nmap -sP 192.168.1.0/24 | nvim

## ssh remote machines
    sudo ssh-keygen -R 192.168.1.x
    ssh-copy-id user@192.168.1.x
    ssh user@192.168.1.x

## Jump Git password (without)
    (https://github.com/losacii/ubuntuMemo/blob/master/ubuntu_note_book.md)
    cd /
    git config --global credential.helper store

=============================================
    http://vim-latex.sourceforge.net/
    https://github.com/vim-latex/vim-latex
    https://danielmiessler.com/study/manually-set-ip-linux

## VirtualBox headless running (in background)
    VBoxManage startvm   Debian10 --type headless
    VBoxManage controlvm Debian10 poweroff
    ping 192.168.1.9
    ssh losacii@192.168.1.9

## rsync: Copy, Sync
rsync -zarP --exclude="*.mp4" --delete ~/gitnote/ losacii@192.168.1.9:~/gitnote/ 
rsync -zarP --exclude="*.mp4" --delete ~/dev/ losacii@192.168.1.9:~/dev/
