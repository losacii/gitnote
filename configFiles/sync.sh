echo "Deleting..."
rm  ~/.bash_aliases
rm  ~/.bashrc
rm  ~/.inputrc
rm  ~/.config/nvim/init.vim
rm  ~/.zshrc
rm  ~/.config/i3/config
rm  ~/.i3status.conf
rm  ~/.config/kitty/kitty.conf
rm  ~/.config/vifm/vifmrc
rm  ~/.xinitrc
#rm  ~/.Spacevim.dBack/init.toml
#rm  ~/.SpacevimBack/config/main.vim

sudo rm /etc/default/keyboard

echo "linking..."

cp          ~/.bash_aliases  confiles/_bash_aliases
cp          ~/.bashrc  confiles/_bashrc                    
sudo cp     /etc/default/keyboard  confiles/_etc.default.keyboard
cp          ~/.config/i3/config  confiles/_i3config          
cp          ~/.i3status.conf  confiles/_i3status.conf             
cp          ~/.inputrc  confiles/_inputrc                   
cp          ~/.config/nvim/init.vim  vimrc_myConfigs/_nvim_init.vim
cp          ~/.inputrc  confiles/_inputrc
cp          ~/.config/kitty/kitty.conf  confiles/_kittyConfig   
cp -r       ~/.myScripts/  ~/confiles/myScripts/
cp          ~/.config/vifm/vifmrc  confiles/_vifmrc        
cp          ~/.zshrc  confiles/_zshrc                     
cp          ~/.xinitrc  confiles/_xinitrc                   

sudo cp   /usr/share/keymaps/i386/qwerty/us.kmap.gz   confiles/us.kmap.gz
