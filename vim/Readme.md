To your `.vimrc` you should add

```
au BufNewFile,BufRead *.cwl setlocal ft=cwl
```

(You can check if this works properly by loading a `cwl` file and executing `:set ft?`. Verify that it returns 
`filetype=cwl`)



`:PlugStatus` - check if the plugin took.



```
if executable('benten-ls')
    au User lsp_setup call lsp#register_server({
        \ 'name': 'cwl',
        \ 'cmd': {server_info->['benten-ls']},
        \ 'whitelist': ['cwl'],
        \ })
endif
```

An minimally functional `.vimrc` file (mine) is

```
syntax on

au BufNewFile,BufRead *.cwl setlocal ft=cwl

" Specify a directory for plugins
" - For Neovim: ~/.local/share/nvim/plugged
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')

" Make sure you use single quotes

Plug 'prabirshrestha/async.vim'
Plug 'prabirshrestha/vim-lsp'

call plug#end()

let g:lsp_log_verbose = 1
let g:lsp_log_file = expand('~/vim-lsp.log')

if executable('benten-ls')
    au User lsp_setup call lsp#register_server({
        \ 'name': 'cwl',
        \ 'cmd': {server_info->['benten-ls']},
        \ 'whitelist': ['cwl'],
        \ })
endif
```