git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install

sudo wget \
    https://raw.githubusercontent.com/vim-scripts/Diablo3/master/colors/diablo3.vim \
    https://raw.githubusercontent.com/tomasr/molokai/master/colors/molokai.vim \
    https://raw.githubusercontent.com/vim-scripts/AutumnLeaf/master/colors/autumnleaf.vim \
    -P /usr/share/nvim/runtime/colors/

mkdir -p ~/.config/nvim

cat vimrc > ~/.config/nvim/init.vim

:PlugInstall

pip3 install python-language-server
