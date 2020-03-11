command! RANDTIP : call s:ShowRandomTip()

function! s:ShowRandomTip()
  let rtip = system("python3 /usr/share/nvim/runtime/plugin/tip_me/get_tip.py")
  echom rtip
endfu

