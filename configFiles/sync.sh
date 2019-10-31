
echo "Deleting..."
rm  ~/.bash_aliases              
rm  ~/.bashrc                    
rm  ~/.zshrc                     
rm  ~/.inputrc                   
rm  ~/.config/i3/config          
rm  ~/.i3status.conf             
rm  ~/.config/kitty/kitty.conf   
rm  ~/.config/vifm/vifmrc        
rm  ~/.xinitrc                   
rm  ~/.Spacevim.dBack/init.toml
rm  ~/.SpacevimBack/config/main.vim

sudo rm /etc/default/keyboard


echo "linking..."
sudo ln confiles/_etc.default.keyboard /etc/default/keyboard

ln  confiles/_bash_aliases      ~/.bash_aliases              
ln  confiles/_bashrc            ~/.bashrc                    
ln  confiles/_zshrc             ~/.zshrc                     
ln  confiles/_inputrc           ~/.inputrc                   

ln  confiles/_i3config          ~/.config/i3/config          
ln  confiles/_i3status.conf     ~/.i3status.conf             
ln  confiles/_kittyConfig       ~/.config/kitty/kitty.conf   

ln  confiles/_vifmrc            ~/.config/vifm/vifmrc        
ln  confiles/_xinitrc           ~/.xinitrc                   

ln  confiles/_spaceFVD.vim      ~/.Spacevim.dBack/init.toml
ln  confiles/_spaceMain.vim     ~/.SpacevimBack/config/main.vim

echo "Done!"







