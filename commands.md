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

## VirtualBox headless running (in background)
    VBoxManage startvm Debian10 --type headless


=============================================
    http://vim-latex.sourceforge.net/
    https://github.com/vim-latex/vim-latex
    fzf
    https://danielmiessler.com/study/manually-set-ip-linux/
