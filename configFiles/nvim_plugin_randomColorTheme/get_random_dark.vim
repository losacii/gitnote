command! RANDOMCOLORD : call s:GetRandomColor()

function! s:GetRandomColor()
  let randclr = system("python3 /usr/share/nvim/runtime/plugin/randomColorTheme/getRandomColorName.py dark")
  exe "source " . randclr
  echom "colorsheme set to: " . randclr
endfu

