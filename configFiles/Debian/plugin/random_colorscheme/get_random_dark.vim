command! RANDOMCOLORD : call s:GetRandomColor()

function! s:GetRandomColor()
  let randclr = system("python3 /usr/share/nvim/runtime/plugin/random_colorscheme/getRandomColorName.py dark")
  echom randclr
  exe "source " . randclr
  echom "colorsheme set to: " . randclr
endfu

