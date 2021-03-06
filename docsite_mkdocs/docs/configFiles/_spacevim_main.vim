"=============================================================================
" main.vim --- Main file of SpaceVim
" Copyright (c) 2016-2017 Shidong Wang & Contributors
" Author: Shidong Wang < wsdjeg at 163.com >
" URL: https://spacevim.org
" License: GPLv3
"=============================================================================

" Enable nocompatible
if has('vim_starting')
  " set default encoding to utf-8
  " Let Vim use utf-8 internally, because many scripts require this
  exe 'set encoding=utf-8'
  scriptencoding utf-8
  if &compatible
    set nocompatible
  endif
  " python host
  if !empty($PYTHON_HOST_PROG)
    let g:python_host_prog  = $PYTHON_HOST_PROG
  endif
  if !empty($PYTHON3_HOST_PROG)
    let g:python3_host_prog = $PYTHON3_HOST_PROG
  endif
endif

" Detect root directory of SpaceVim
if has('win16') || has('win32') || has('win64')
  function! s:resolve(path) abort
    let cmd = 'dir /a "' . a:path . '" | findstr SYMLINK'
    " 2018/12/07 周五  下午 10:23    <SYMLINK>      vimfiles [C:\Users\Administrator\.SpaceVim]
    " ref: https://superuser.com/questions/524669/checking-where-a-symbolic-link-points-at-in-windows-7
    silent let rst = system(cmd)
    if !v:shell_error let dir = split(rst)[-1][1:-2]
      return dir
    endif
    return a:path
  endfunction
else
  function! s:resolve(path) abort
    return resolve(a:path)
  endfunction
endif


let g:_spacevim_root_dir = fnamemodify(s:resolve(fnamemodify(expand('<sfile>'),
      \ ':p:h:h:gs?\\?'.((has('win16') || has('win32')
      \ || has('win64'))?'\':'/') . '?')), ':p:gs?[\\/]?/?')
lockvar g:_spacevim_root_dir
if has('nvim')
  let s:qtdir = split(&rtp, ',')[-1]
  if s:qtdir =~# 'nvim-qt'
    let &rtp = s:qtdir . ',' . g:_spacevim_root_dir . ',' . $VIMRUNTIME
  else
    let &rtp = g:_spacevim_root_dir . ',' . $VIMRUNTIME
  endif
else
  let &rtp = g:_spacevim_root_dir . ',' . $VIMRUNTIME
endif

call SpaceVim#begin()

call SpaceVim#custom#load()

call SpaceVim#end()
" vim:set et sw=2 cc=80:

"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ VI'S Settings ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
let mapleader=','
nnoremap <leader>rr :!clang % && ./a.out<cr>

nnoremap <leader>rc :tabnew ~/.SpaceVim/config/main.vim<cr>

" color themes: anokha, diablo3
colorscheme anokha
nnoremap <F2> :execute "colorscheme ".getline('.')<cr>
nnoremap <F4> jmxkddggP'xzz
nnoremap <F5> jmxkddGP'xzz


" colorschemes:  show | pick  
nnoremap ;cd :RANDOMCOLORD<cr>
nnoremap ;cl :RANDOMCOLORL<cr>


"   random pick
nnoremap ;cc :28vs ~/Documents/gitnote/configFiles/vim_color_themes/clrs<cr>

"save file, exit file, exit vim
nnoremap <leader>w :up<cr>
nnoremap ;fw :up<cr>
nnoremap ;fe :q!<cr>
nnoremap ;ee :qa!<cr>
nnoremap ;x :xa<cr>

nnoremap <leader>o :tabnew <space>

" Move cursors
inoremap è <Left>
inoremap ê <Down>
inoremap ë <Up>
inoremap ì <Right>
inoremap <m-h> <Left>
inoremap <m-j> <Down>
inoremap <m-k> <Up>
inoremap <m-l> <Right>
inoremap <m-i> <left><left><left><left><left>
inoremap <m-o> <right><right><right><right><right>
inoremap <m-u> <esc>0i
inoremap <m-p> <esc>$a

inoremap é <esc>Bi
inoremap ï <esc>Wa
inoremap õ <home>
inoremap ð <end>

nnoremap cw ciw
nnoremap dw diw
nnoremap vw viw
nnoremap vl 0v$
nnoremap vs vis

nnoremap <C-A> ggVG
nnoremap Y y$$
nnoremap yp yyP
nnoremap yb mmvBy`mp

nnoremap <leader>rp :%w !python3<cr>
nnoremap <leader>pr o'''<esc>yypk:r!python3 %<cr>
nnoremap ;rr :%s///g<left><left>

nnoremap t, :tabNext<cr>
nnoremap t. :tabnext<cr>
nnoremap ;snp :tabnew ~/.cache/vimfiles/repos/github.com/Shougo/neosnippet-snippets/neosnippets/_.snip

" open file in new tab
nnoremap ,to :execute "tabnew ".getline('.')

" Current line as VIM Operation:  "oyy@o   yy@"
" Current line as Ex Command:     :execute getline(".")

" Current
:vnoremap <f2> :<c-u>exe join(getline("'<","'>"),'<bar>')<cr>

" Swap this line and 'x-line
nnoremap <leader>rl ddmy'xPjdd'yP


" Swap two Words: mm <leader>rw
nnoremap <leader>rW mnviW"ny`mviW"myviW"np`nviW"mp
nnoremap <leader>rw mnviw"ny`mviw"myviw"np`nviw"mp

" move Word / right left
nnoremap <m-l> diWmaEviWp`aPE

" Surround a word with []
nnoremap ;x viwxi[]<esc>P
vnoremap ;x xi[]<esc>P

set ignorecase

" auto number increment
nnoremap <leader>a yyp:.s/\d\+/\=submatch(0)+1/g<cr>

" source this buffer!!!
nnoremap <leader>vs ggVGy:@"<CR>

" { } behavior
nnoremap } }zzj<c-e>
nnoremap { {{jzz<c-y>

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

:set sessionoptions=blank,winsize,tabpages,resize

" Current line as url, Open it with Chromium!
nnoremap gx :exe ':silent !chromium '.getline('.')<CR>

" Visual-selection! Google Search it
function! GoogleSearch()
     let searchterm = getreg("g")
     silent! exec "silent! !chromium \"http://google.com/search?q=" . searchterm . "\" &"
endfunction
vnoremap gs "gy<Esc>:call GoogleSearch()<CR>
