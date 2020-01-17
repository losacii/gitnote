command! RANDOMCOLORL : call s:GetRandomLight()

function! s:GetRandomLight()
  let randclr = system("python3 /usr/share/nvim/runtime/plugin/randomColorTheme/getRandomColorName.py light")
  exe "source " . randclr
  echom "colorsheme set to: " . randclr
endfu

