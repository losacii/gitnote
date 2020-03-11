command! RANDOMCOLORL : call s:GetRandomColor()

function! s:GetRandomColor()
  let randclr = system("python3 /usr/share/nvim/runtime/plugin/random_colorscheme/getRandomColorName.py light")
  echom randclr
  exe "source " . randclr
  echom "colorsheme set to: " . randclr
endfu

