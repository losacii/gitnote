" For snippets: ~/.config/nvim/UltiSnips/

" Vim-Plug
call plug#begin('~/.vim/plugged')

    Plug 'neoclide/coc.nvim', {'branch': 'release'}

    Plug 'scrooloose/nerdtree'
    Plug 'tiagofumo/vim-nerdtree-syntax-highlight'

    Plug 'scrooloose/nerdcommenter'

    Plug 'chun-yang/auto-pairs'
    "Plug 'prettier/vim-prettier', { 'do': 'yarn install' }

    Plug 'HerringtonDarkholme/yats.vim' " TS Syntax

    Plug 'morhetz/gruvbox'

    "  ----- FZF -----
    " https://github.com/junegunn/fzf.vim   
    " In Terminal, Ctrl+t,  Esc > c
    " --> Commands: Files Colors Ag
    " Rg(alt-a alt-d)
    Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
    Plug 'junegunn/fzf.vim'
    if executable('fzf')
        nnoremap <c-p> :FZF -e<cr>
    endif

    " ----- GlyGrep -----
    " And, FlyGrep  :FlyGrep (instead of ark!)
    " https://github.com/wsdjeg/FlyGrep.vim  c-a c-e c-j c-k
    Plug 'wsdjeg/FlyGrep.vim'
    nnoremap <leader>rg :FlyGrep<cr>

    " Easy-Motion
    Plug 'easymotion/vim-easymotion'

    " highlight yank
    Plug 'machakann/vim-highlightedyank'
    Plug 'tpope/vim-surround'

    Plug 'prabirshrestha/async.vim'
    Plug 'Flowerowl/ici.vim'
    Plug 'roxma/nvim-yarp'

    Plug 'bling/vim-airline'

    set completeopt=noinsert,menuone,noselect 

    Plug 'leafgarland/typescript-vim'
    Plug 'ianks/vim-tsx'

" Initialize plugin system
call plug#end()

" Terminal Colors
set t_Co=256
syntax on
colorscheme gruvbox

" mapleader
let mapleader=','
set pastetoggle=<F12>

" Super Powers
nnoremap <leader>a :AUTOINCLINE<cr>

" Python print this line value
nnoremap <leader>vp :execute "!python3 -c 'print(" .getline('.') . ")'"<CR>

"Yank!
nnoremap yp :COPYLINEDOWN<cr>
nnoremap Y y$$
nnoremap yb mmvBhy`mp
nnoremap <c-a> ggVG

inoremap jk <ESC>
inoremap kj <ESC>

" open NERDTree automatically
" autocmd StdinReadPre * let s:std_in=1
" autocmd VimEnter * NERDTree

let g:NERDTreeIgnore = ['^node_modules$']

" ~ ~ ~ ~ ~ ~ ~ ~ COC: Jump to placeholders
" jump to next placeholder, <C-j> is default of coc.nvim 
let g:coc_snippet_next = '<c-j>'

" jump to previous placeholder, <C-k> is default of coc.nvim
let g:coc_snippet_prev = '<c-k>'

" vim-prettier
"let g:prettier#quickfix_enabled = 0
"let g:prettier#quickfix_auto_focus = 0
" prettier command for coc
command! -nargs=0 Prettier :CocCommand prettier.formatFile
" run prettier on save
"let g:prettier#autoformat = 0
"autocmd BufWritePre *.js,*.jsx,*.mjs,*.ts,*.tsx,*.css,*.less,*.scss,*.json,*.graphql,*.md,*.vue,*.yaml,*.html PrettierAsync


" ctrlp
let g:ctrlp_user_command = ['.git/', 'git --git-dir=%s/.git ls-files -oc --exclude-standard']

" j/k will move virtual lines (lines that wrap)
noremap <silent> <expr> j (v:count == 0 ? 'gj' : 'j')
noremap <silent> <expr> k (v:count == 0 ? 'gk' : 'k')

set number
set relativenumber

" sync open file with NERDTree
" " Check if NERDTree is open or active
function! IsNERDTreeOpen()
  return exists("t:NERDTreeBufName") && (bufwinnr(t:NERDTreeBufName) != -1)
endfunction

" Call NERDTreeFind iff NERDTree is active, current window contains a modifiable
" file, and we're not in vimdiff
function! SyncTree()
  if &modifiable && IsNERDTreeOpen() && strlen(expand('%')) > 0 && !&diff
    NERDTreeFind
    wincmd p
  endif
endfunction

" Highlight currently open buffer in NERDTree
autocmd BufEnter * call SyncTree()

" coc config
let g:coc_global_extensions = [
  \ 'coc-json',
  \ 'coc-html',
  \ 'coc-css',
  \ 'coc-emmet',
  \ 'coc-eslint',
  \ 'coc-tslint',
  \ 'coc-tsserver',
  \ 'coc-snippets',
  \ 'coc-python',
  \ 'coc-word', 
  \ 'coc-dictionary', 
  \ 'coc-prettier', 
  \ ]

" from readme
" if hidden is not set, TextEdit might fail.
set hidden " Some servers have issues with backup files, see #649 set nobackup set nowritebackup " Better display for messages set cmdheight=2 " You will have bad experience for diagnostic messages when it's default 4000.

" don't give |ins-completion-menu| messages.
set shortmess+=c

" always show signcolumns
set signcolumn=yes

" Use tab for trigger completion with characters ahead and navigate.
" Use command ':verbose imap <tab>' to make sure tab is not mapped by other plugin.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
inoremap <silent><expr> <c-space> coc#refresh()
inoremap <space> <nop>


" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current position.
" Coc only does snippet and additional edit on confirm.
inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
" Or use `complete_info` if your vim support it, like:
" inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"

" Use `[g` and `]g` to navigate diagnostics
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" Remap keys for gotos
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

" Highlight symbol under cursor on CursorHold
autocmd CursorHold * silent call CocActionAsync('highlight')

" Remap for rename current word
nmap <F2> <Plug>(coc-rename)

augroup mygroup
  autocmd!
  " Setup formatexpr specified filetype(s).
  autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  " Update signature help on jump placeholder
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Remap for format selected region
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

" Create mappings for function text object, requires document symbols feature of languageserver.
xmap if <Plug>(coc-funcobj-i)
xmap af <Plug>(coc-funcobj-a)
omap if <Plug>(coc-funcobj-i)
omap af <Plug>(coc-funcobj-a)

" Use <C-d> for select selections ranges, needs server support, like: coc-tsserver, coc-python
nmap <silent> <C-d> <Plug>(coc-range-select)
xmap <silent> <C-d> <Plug>(coc-range-select)

" Use `:Format` to format current buffer
command! -nargs=0 Format :call CocAction('format')

" Use `:Fold` to fold current buffer
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" use `:OR` for organize import of current buffer
command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')

" Add status line support, for integration with other plugin, checkout `:h coc-status`
set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}






" change window focus
nnoremap <space><space> :bnext<cr>
nnoremap <space>h <c-w>h
nnoremap <space>j <c-w>j
nnoremap <space>k <c-w>k
nnoremap <space>l <c-w>l


" open rc file
nnoremap <leader>rc :tabnew $MYVIMRC<CR>

vnoremap <F8> "+y:!python3 ~/gitnote/Python/auto_input.py<cr>


" ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

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
set list listchars=tab:▸\ ,eol:¬

" Basic
set autoindent
set smartindent
set showcmd
set ruler      " show cursor position all the time
set cursorline " hignlight cursor-line

set encoding=utf-8

" tab settings
set nowrap
set shiftwidth=2
set tabstop=2
set softtabstop=2
set expandtab
set smarttab

nnoremap g. :tabnext<cr>
nnoremap g, :tabNext<cr>
nnoremap <leader>to :tabnew <space>

" Disable Anoying auto Visual mode Feature!!!
set mouse-=a

" backspace over everything in instert mode
set backspace=indent,eol,start

" keys modify
nnoremap j gj
nnoremap k gk

nnoremap cw ciw
nnoremap dw diw
nnoremap vw viW
nnoremap yl 0y$
nnoremap dl ^d$
nnoremap vv 0v$

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
nnoremap vv 0v$

"  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ set color for text width ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
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
nnoremap gw viwy:Ici 0
nnoremap gW viw"gy<Esc>:!python3 ~/gitnote/pyDictionary/_forVim.py <c-r>g<CR>

set ignorecase

" AUTO SAVE FOLDS
augroup AutoSaveFolds
  autocmd!
  " view files are about 500 bytes
  " bufleave but not bufwinleave captures closing 2nd tab
  " nested is needed by bufwrite* (if triggered via other autocmd)
  autocmd BufWinLeave,BufLeave,BufWritePost ?* nested silent! mkview!
  autocmd BufWinEnter ?* silent! loadview
augroup end

" change window focus
nnoremap <space><space> <c-w>w
nnoremap <space>h <c-w>h
nnoremap <space>j <c-w>j
nnoremap <space>k <c-w>k
nnoremap <space>l <c-w>l

nnoremap z<space> za

map ; <Plug>(easymotion-prefix)

" Undo file after reopening
set undofile
set undodir=/tmp

" Move cursors
inoremap ˙ <Left>
inoremap ∆ <Down>
inoremap ˚ <Up>
inoremap ¬ <Right>
inoremap <m-h> <Left>
inoremap <m-j> <Down>
inoremap <m-k> <Up>
inoremap <m-l> <Right>

inoremap <m-i> <esc>4hi
inoremap <m-o> <esc>5la
inoremap ˆ <left><left><left><left><left>
inoremap ø <right><right><right><right><right>

inoremap <m-,> <esc>0i
inoremap <m-.> <esc>$a
inoremap ≤ <esc>0i
inoremap ≥ <esc>$a


set sessionoptions=blank,winsize,tabpages,resize

vnoremap y "+y
nnoremap <m-i> "+P

" Better w and b (word forward/back)
nnoremap w /\w\+<cr>:noh<cr>
nnoremap b ?\w\+<cr>:noh<cr>

" Upper Case
nnoremap ;u viwUe
inoremap ;u <esc>viwUea


" Folding
set foldmethod=manual
set foldnestmax=10
set nofoldenable
set foldlevel=2

" Undo history dir
set hid
set undodir=~/.vim/undodir
set undofile
set viewoptions=folds,cursor
set sessionoptions=folds

set nobackup nowritebackup

"" Timer
"let timer = timer_start(7000, 'TimerHandle',{'repeat':-1})
"func! TimerHandle(timer)
"  RANDTIP
"endfunc

set updatetime=5000
autocmd CursorHold * RANDTIP


""~ ~ ~ ~ ~ ~ ~ ~ ~ ~ VI'S Settings ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
"
" Swap this line and 'x-line
nnoremap <leader>rl ddmy'xPjdd'yP

" is his thoughtless; taste he is banal habits in restraints his housekeeping and a horror

" move Word / right left
nnoremap <m-l> diWmaEviWp`aPEb
nnoremap <m-h> EBBdiWmaEviWp`aPEbB

" Surround a with word []
nnoremap ;x viwxi[]<esc>P
vnoremap ;x xi[]<esc>P

" Clang run program!
"nnoremap <leader>rr :!clang % && ./a.out<cr>
"" color themes: anokha, diablo3

"nnoremap <F4> jmxkddggP'xzz
"nnoremap <F5> jmxkddGP'xzz

"" colorschemes:  show | pick  
"nnoremap ;cd :RANDOMCOLORD<cr>
"nnoremap ;cl :RANDOMCOLORL<cr>
"
"
""   random pick
"nnoremap ;cc :28vs ~/Documents/gitnote/configFiles/vim_color_themes/clrs<cr>

