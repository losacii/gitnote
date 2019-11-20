
echo "Deleting..."
rm ~/.bash_aliases              
rm ~/.bashrc                    
rm ~/.inputrc                   
rm ~/.config/nvim/init.vim
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

ln  confiles/_bash_aliases      ~/.bash_aliases              
cp  confiles/_bashrc            ~/.bashrc                    
ln  confiles/_inputrc           ~/.inputrc                   
ln  confiles/_vimrc             ~/.config/nvim/init.vim

#ln  confiles/_zshrc             ~/.zshrc                     

cp  confiles/_i3config          ~/.config/i3/config          
cp  confiles/_i3status.conf     ~/.i3status.conf             
cp  confiles/_kittyConfig       ~/.config/kitty/kitty.conf   

ln  confiles/_vifmrc            ~/.config/vifm/vifmrc        
#ln  confiles/_xinitrc           ~/.xinitrc                   

#ln  confiles/_spaceFVD.vim      ~/.Spacevim.dBack/init.toml
#ln  confiles/_spaceMain.vim     ~/.SpacevimBack/config/main.vim

sudo cp confiles/_etc.default.keyboard /etc/default/keyboard
echo "Done!"

sudo cp   ~/gitnote/configFiles/confiles/us.kmap.gz   /usr/share/keymaps/i386/qwerty/us.kmap.gz




