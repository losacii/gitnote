echo "deleting..."
rm  ~/.bash_aliases
rm  ~/.bashrc
rm  ~/.config/i3/config
rm  ~/.config/vifm/vifmrc
rm  ~/.i3status.conf
rm  ~/.inputrc
rm  ~/.config/kitty/kitty.conf
rm  ~/.SpaceVim.d/init.toml
rm  ~/.SpaceVim/config/main.vim
rm  ~/.xinitrc
rm  ~/.config/vifm/vifmrc
sudo rm /etc/default/keyboard

echo "linking..."
ln              confiles/_bash_aliases  ~/.bash_aliases
ln                    confiles/_bashrc  ~/.bashrc
ln          confiles/_i3config  ~/.config/i3/config
ln        confiles/_vifmrc  ~/.config/vifm/vifmrc
ln             confiles/_i3status.conf  ~/.i3status.conf
ln                   confiles/_inputrc  ~/.inputrc
ln   confiles/_kittyConfig  ~/.config/kitty/kitty.conf
ln      confiles/_spaceFVD.vim  ~/.SpaceVim.d/init.toml
ln  confiles/_spaceMain.vim  ~/.SpaceVim/config/main.vim
ln                   confiles/_xinitrc  ~/.xinitrc
ln        confiles/_vifmrc  ~/.config/vifm/vifmrc
ln       ~/.zshrc   confiles/_zshrc
sudo    ln confiles/_etc.default.keyboard /etc/default/keyboard

echo "Done!"
