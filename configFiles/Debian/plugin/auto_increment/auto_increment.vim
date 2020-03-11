command! AUTOINCLINE : call s:AutoIncLine()

function! s:AutoIncLine()
  let row  = getpos('.')[1]
  let clmn = getpos('.')[2]
  t.
  .s/\d\+/\=(submatch(0)+1)/g
  call cursor(row + 1, clmn)
endfu



command! COPYLINEDOWN : call s:CopyLineDown()

function! s:CopyLineDown()
  let row  = getpos('.')[1]
  let clmn = getpos('.')[2]
  t.
  call cursor(row + 1, clmn)
endfu

