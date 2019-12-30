
echo "Deleting..."
mv  ~/.bash_aliases  ~/.bash_aliases.bak
mv  ~/.bashrc  ~/.bashrc.bak
mv  ~/.inputrc  ~/.inputrc.bak
mv  ~/.config/nvim/init.vim  ~/.config/nvim/init.vim.bak
mv  ~/.zshrc  ~/.zshrc.bak
mv  ~/.config/i3/config  ~/.config/i3/config.bak
mv  ~/.i3status.conf  ~/.i3status.conf.bak
mv  ~/.config/kitty/kitty.conf  ~/.config/kitty/kitty.conf.bak
mv  ~/.config/vifm/vifmrc  ~/.config/vifm/vifmrc.bak
mv  ~/.xinitrc  ~/.xinitrc.bak
#rm  ~/.Spacevim.dBack/init.toml
#rm  ~/.SpacevimBack/config/main.vim

sudo rm /etc/default/keyboard

echo "linking..."

ln  confiles/_bash_aliases      ~/.bash_aliases              
ln  confiles/_bashrc            ~/.bashrc                    
ln  confiles/_inputrc           ~/.inputrc                   
ln  confiles/_nvim_init.vim     ~/.config/nvim/init.vim
ln  confiles/_zshrc             ~/.zshrc                     
ln  confiles/_i3config          ~/.config/i3/config          
ln  confiles/_i3status.conf     ~/.i3status.conf             
ln  confiles/_kittyConfig       ~/.config/kitty/kitty.conf   
ln  confiles/_vifmrc            ~/.config/vifm/vifmrc        
ln  confiles/_xinitrc           ~/.xinitrc                   

sudo cp confiles/_etc.default.keyboard /etc/default/keyboard
sudo cp   /usr/share/keymaps/i386/qwerty/us.kmap.gz   confiles/us.kmap.gz
