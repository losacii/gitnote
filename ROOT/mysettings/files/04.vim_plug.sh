mkdir -p ~/.config/nvim
cat vimrc > ~/.config/nvim/init.vim

sudo wget \
    https://raw.githubusercontent.com/vim-scripts/Diablo3/master/colors/diablo3.vim \
    https://raw.githubusercontent.com/tomasr/molokai/master/colors/molokai.vim \
    https://raw.githubusercontent.com/vim-scripts/AutumnLeaf/master/colors/autumnleaf.vim \
    -P /usr/share/nvim/runtime/colors/
