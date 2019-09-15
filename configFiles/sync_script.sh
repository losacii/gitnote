# Files starts with _
# cd this directory
# ~/.cache/vimfiles/repos/github.com/Shougo/neosnippet-snippets/neosnippets

mkdir ~/.myScripts/

rm ~/.bash_aliases
rm ~/.bashrc
rm ~/.config/i3/config
rm ~/.inputrc
# rm ~/.config/kitty/kitty.conf
rm ~/.SpaceVim.d/init.toml
rm ~/.SpaceVim/config/main.vim
rm ~/.xinitrc

cp _bash_aliases ~/.bash_aliases
cp _bashrc ~/.bashrc
cp _i3config ~/.config/i3/config
cp _inputrc ~/.inputrc
# cp _kitty.conf ~/.config/kitty/kitty.conf
cp _spacevim_FVD ~/.SpaceVim.d/init.toml
cp _spacevim_main.vim ~/.SpaceVim/config/main.vim
cp _xinitrc ~/.xinitrc
ln _my_custom_commands.txt ~/.myScripts/my_custom_commands.sh
