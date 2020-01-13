"mapleader
let mapleader=','
set pastetoggle=<F12>

autocmd BufNewFile *.txt :echom "text(txt-type) file Buffer!"

nnoremap <F8> "+yy:!python3 ~/gitnote/Python/auto_input.py<cr>

" open rc file
nnoremap <leader>rc :tabnew $MYVIMRC<CR>

inoremap kj <c-c>
inoremap jk <c-c>

" line number
set nu rnu

" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.local/share/nvim/plugged')

    " Make sure you use single quotes
    Plug 'scrooloose/nerdtree'
    autocmd StdinReadPre * let s:std_in=1
    autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
    "Commenter <leader>c<cpace>
    Plug 'mattn/emmet-vim'
    Plug 'scrooloose/nerdcommenter'
    Plug 'vim-scripts/nc.vim'
    " Beautify Status Bar
    Plug 'bling/vim-airline'
    " Plugin outside ~/.vim/plugged with post-update hook
    " https://github.com/junegunn/fzf.vim 
    " In Terminal, Ctrl+t,  Esc > c
    " --> Commands: Files Colors Ag
    " Rg(alt-a alt-d)
    Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
    Plug 'junegunn/fzf.vim'
    if executable('fzf')
        nnoremap <c-p> :FZF -e<cr>
    endif
    " And, FlyGrep  :FlyGrep (instead of ark!)
    " https://github.com/wsdjeg/FlyGrep.vim  c-a c-e c-j c-k
    Plug 'wsdjeg/FlyGrep.vim'
    nnoremap <leader>rg :FlyGrep<cr>
    "Color Theme
    Plug 'tomasr/molokai'
    "Auto Pair
    Plug 'jiangmiao/auto-pairs'
    " vim-sneak:  s<char><char> ; 3; `` s<enter>
    " https://github.com/justinmk/vim-sneak
    Plug 'justinmk/vim-sneak'
    Plug 'easymotion/vim-easymotion'
    " highlight yank
    Plug 'machakann/vim-highlightedyank'
    Plug 'tpope/vim-surround'
    " Plug 'tpope/fugitive'   " git utils......
    
    " Language Server Protocal
    " vim-lsp: https://github.com/prabirshrestha/vim-lsp 
    " ncm2:  https://github.com/ncm2/ncm2
    Plug 'Flowerowl/ici.vim'
    Plug 'prabirshrestha/async.vim'
    Plug 'prabirshrestha/vim-lsp'
    Plug 'roxma/nvim-yarp'
    Plug 'ncm2/ncm2'
    Plug 'ncm2/ncm2-vim-lsp'
    Plug 'filipekiss/ncm2-look.vim'
    let g:ncm2_look_enabled = 1

    autocmd BufEnter * call ncm2#enable_for_buffer()

    "" pop up information
    set completeopt=noinsert,menuone,noselect 
    Plug 'ncm2/ncm2-bufword'
    Plug 'ncm2/ncm2-path'

    if executable('pyls')
    " pip install python-language-server
    au User lsp_setup call lsp#register_server({
        \ 'name': 'pyls',
        \ 'cmd': {server_info->['pyls']},
        \ 'whitelist': ['python3', 'python'],
        \ })
    endif
    let g:lsp_diagnostics_enabled = 0         " disable diagnostics support
    let g:lsp_signs_enabled = 0         " enable signs
    let g:lsp_diagnostics_echo_cursor = 1 " enable echo under cursor when in normal mode
    let g:lsp_signs_error = {'text': '✗'}
    " ncm2: Use <TAB> to select the popup menu:
    inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
    inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

    " Track the engine.
    Plug 'SirVer/ultisnips'

    " Snippets are separated from the engine. Add this if you want them:
    Plug 'honza/vim-snippets'

    " Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.
    let g:UltiSnipsExpandTrigger="<tab>"
    let g:UltiSnipsJumpForwardTrigger="<m-n>"
    let g:UltiSnipsJumpBackwardTrigger="<m-m>"

    " If you want :UltiSnipsEdit to split your window.
    let g:UltiSnipsEditSplit="vertical"

"Initialize plugin system
call plug#end()

source ~/gitnote/configFiles/vim_color_themes/dark/diablo3.vim

"Yank!
nnoremap yp yyp
nnoremap Y y$$
nnoremap yb mxvBy`xp
nnoremap <c-a> ggVG

"" Swap two Words: mm <leader>rw
nnoremap <leader>sw my`x"xyiw`yviw"xp`xviwp`y
"mnviW"ny`mviW"myviW"np`nviW"mp
"nnoremap <leader>rw mnviw"ny`mviw"myviw"np`nviw"mp

"Split Toggle
nnoremap <space><space> <c-w>w
nnoremap <space>w <c-w>

"File Tree
nnoremap <space>/ :NERDTreeToggle<cr>

"Save & Quit
nnoremap <leader>w :update<cr>
nnoremap <leader>x :q!<cr>
nnoremap <leader>ee :qa!<cr>

"Toggle Line Number
nnoremap <space>nn :set nu! rnu!<cr>

" show enter-char etc..
" set list
" set list listchars=tab:▸\ ,eol:¬

" Basic
set autoindent
set smartindent
set showcmd
set ruler      " show cursor position all the time
set cursorline " hignlight cursor-line

set encoding=utf-8

" tab settings
set nowrap
set shiftwidth=4
set tabstop=4
set softtabstop=4
set expandtab
set smarttab
nnoremap g. :tabnext<cr>
nnoremap g, :tabNext<cr>

" Disable Anoying auto Visual mode Feature!!!
set mouse-=a

" backspace over everything in instert mode
set backspace=indent,eol,start

" keys modify
nnoremap j gj
nnoremap k gk

nnoremap cw ciw
nnoremap dw diw
nnoremap vw viw
nnoremap vs vis
nnoremap dl 0d$

nnoremap H Hjj
nnoremap L Lkk
nnoremap <m-j> }
nnoremap <m-k> {


" Buffers
nnoremap <space>bn :bnext<cr>
nnoremap <space>bp :bprevious<cr>
nnoremap <space>tp :tabnext<cr>
nnoremap <space>tp :tabNext<cr>
nnoremap <space>w <c-w>

" git commands
nnoremap ,ga :!git add .
nnoremap ,gc :!git commit -m ""<left>
nnoremap ,gp :!git push
" os clipboard sharing
set clipboard=unnamed

" Undo file after reopening
set undofile
set undodir=/tmp

" navigate tabs
nnoremap <left> :tabprevious<cr>
nnoremap <right> :tabnext<cr>

nnoremap vv 0v$

"  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ set color for text width ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
"  " Text width settings
"  set textwidth=78
"  set colorcolumn=78
"  
"  nnoremap <leader>cw :call ToggleColumnWidth()<cr>
"  let g:wide_column = 1
"  function! ToggleColumnWidth()
"      if g:wide_column
"          set textwidth=100
"          set colorcolumn=100
"          let g:wide_column = 0
"      else
"          set textwidth=80
"          set colorcolumn=80
"          let g:wide_column = 1
"      endif
"  endfunction
highlight ColorColumn ctermbg=magenta
call matchadd('ColorColumn', '\%81v', 81)

set formatoptions=qrnl

" sort lines
nnoremap <leader>st :'<,'>!sort -f<cr>

nnoremap <leader>rr :%s///g<left><left>


" Current line as url, Open it with Chromium!
nnoremap gx :exe ':silent !chromium '.getline('.')<CR>

" Visual-selection! Google Search it
function! GoogleSearch()
     let searchterm = getreg("g")
     silent! exec "silent! !chromium \"http://google.com/search?q=" . searchterm . "\" &"
endfunction
vnoremap gs "gy<Esc>:call GoogleSearch()<CR>

" English Definition of this word!!
nnoremap gw viw"gy<Esc>:execute "Ici ".getreg("g")<CR>
nnoremap gW viw"gy<Esc>:!python3 ~/gitnote/pyDictionary/_forVim.py <c-r>g<CR>

" { } behavior
nnoremap } }zzj<c-e>
nnoremap { {{jzz<c-y>

set ignorecase

" AUTO SAVE FOLDS
augroup remember_folds
  autocmd!
  autocmd BufWinLeave *.* mkview
  autocmd BufWinEnter * silent! loadview
augroup END

" change window focus
nnoremap <space><space> <c-w>w
nnoremap <space>h <c-w>h
nnoremap <space>j <c-w>j
nnoremap <space>k <c-w>k
nnoremap <space>l <c-w>l

nnoremap gw viwy:Ici 0
nnoremap z<space> za

map ; <Plug>(easymotion-prefix)
" Move cursors
inoremap ˙ <Left>
inoremap ∆ <Down>
inoremap ˚ <Up>
inoremap ¬ <Right>
inoremap <m-h> <Left>
inoremap <m-j> <Down>
inoremap <m-k> <Up>
inoremap <m-l> <Right>

inoremap <m-i> <left><left><left><left><left>
inoremap <m-o> <right><right><right><right><right>
inoremap ˆ <left><left><left><left><left>
inoremap ø <right><right><right><right><right>

inoremap <m-,> <esc>0i
inoremap <m-.> <esc>$a
inoremap ≤ <esc>0i
inoremap ≥ <esc>$a


set sessionoptions=blank,winsize,tabpages,resize

" for html
nnoremap {% i{%<space><space>%}<left><left><left>
nnoremap yt yat

""~ ~ ~ ~ ~ ~ ~ ~ ~ ~ VI'S Settings ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
" Clang run program!
"nnoremap <leader>rr :!clang % && ./a.out<cr>
"" color themes: anokha, diablo3
vnoremap <F2> "+y

"nnoremap <F4> jmxkddggP'xzz
"nnoremap <F5> jmxkddGP'xzz

"" colorschemes:  show | pick  
"nnoremap ;cd :RANDOMCOLORD<cr>
"nnoremap ;cl :RANDOMCOLORL<cr>
"
"
""   random pick
"nnoremap ;cc :28vs ~/Documents/gitnote/configFiles/vim_color_themes/clrs<cr>
"
""save file, exit file, exit vim
"nnoremap ;fw :up<cr>
"nnoremap ;fe :q!<cr>
"nnoremap ;ee :qa!<cr>
"nnoremap ;x :xa<cr>
"
nnoremap <leader>o :tabnew <space>
"
"
"nnoremap <C-A> ggVG
"nnoremap Y y$$
"nnoremap yp yyP
"nnoremap yb mmvBy`mp
"
"nnoremap <leader>rp :%w !python3<cr>
" Python print this line value
nnoremap <leader>vp :execute "!python3 -c 'print(" .getline('.') . ")'"<CR>

"nnoremap <leader>pr o'''<esc>yypk:r!python3 %<cr>
"nnoremap ;rr :%s///g<left><left>
"
"nnoremap t, :tabNext<cr>
"nnoremap t. :tabnext<cr>
"nnoremap ;snp :tabnew ~/.cache/vimfiles/repos/github.com/Shougo/neosnippet-snippets/neosnippets/_.snip
"
"" open file in new tab
"nnoremap ,to :execute "tabnew ".getline('.')
"
"" Current line as VIM Operation:  "oyy@o   yy@"
"" Current line as Ex Command:     :execute getline(".")
"
"" Current
":vnoremap <f2> :<c-u>exe join(getline("'<","'>"),'<bar>')<cr>
"
"" Swap this line and 'x-line
"nnoremap <leader>rl ddmy'xPjdd'yP
"

"" move Word / right left
"nnoremap <m-l> diWmaEviWp`aPE
"
"" Surround a word with []
"nnoremap ;x viwxi[]<esc>P
"vnoremap ;x xi[]<esc>P
"
