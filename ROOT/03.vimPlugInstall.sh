git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install


sudo wget \
    https://raw.githubusercontent.com/vim-scripts/Diablo3/master/colors/diablo3.vim \
    https://raw.githubusercontent.com/tomasr/molokai/master/colors/molokai.vim \
    https://raw.githubusercontent.com/vim-scripts/AutumnLeaf/master/colors/autumnleaf.vim \
    -P /usr/share/nvim/runtime/colors/


curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim  


(pwd)
mkdir -p ~/.config/nvim
cp init.vim ~/.config/nvim/

python3 -m pip install pynvim

nvim > PlugInstall


# https://github.com/palantir/python-language-server<Paste>
pip3 install python-language-server
OR
pip3 install 'python-language-server[pycodestyle]'






