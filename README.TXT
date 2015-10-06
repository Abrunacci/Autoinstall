# This file was made only as a guide to complete the custom system configuration.
# Login as root (su) and execute 'sh CustomConfig.sh'
#
#
# The first file who will appear on VIM it's 'pg_hba.conf'
# in this file we go the IPv4 Configuration and change it.
# BEFORE:
host    all             all             127.0.0.1/32            md5
# AFTER:
host    all             all             0.0.0.0/0            md5
#
# Save and exit.
#
########################################################################
#
# The second file it's gonna be 'postgresql.conf'
# We have to search 'listen_addresses' and change it.
# BEFORE:
#listen_addresses = 'localhost' 
# AFTER:
listen_addresses = '*'
#
# IMPORTANT: the line 'listen_addresses' should be uncommented
#
# Save and exit.
#
#########################################################################
#
# Next file will be '.zshrc'
#
# We can change the theme on the line 'ZSH_THEME'
# To see more themes check: https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
#
 ZSH_THEME="themename"
# 
# Recomended theme: 'miloshadzic'
# 
# And we can add plugins
# To see what plugin you can add check: https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins
#
plugins=(pluginName pluginName2)
#
# Recomended plugins: common-aliases debian django git pip python sudo systemd virtualenvwrapper zsh-syntax-highlighting
#
# There are more options to configure but so far only configure these two.
#
###########################################################################
#
# The last file is the .vimrc configuration 
#
# The script creates all the folders and clone the vim-jedi, vim-powerline, wombat256bot and pathogen.
#
#
# Now we have to uncomment some lines. 
# (Once again, this is just an example and you can uncomment whatever line you want)
#
# We will uncomment the next sections
#
" Quicksave command
noremap <C-Z> :update<CR>
vnoremap <C-Z> <C-C>:update<CR>
inoremap <C-Z> <C-O>:update<CR>
#
" Color scheme
set t_Co=256
color wombat256mod
#
" Enable syntax highlighting
filetype off
filetype plugin indent on
syntax on
#
" Showing line numbers and length
set number  " show line numbers
set tw=79   " width of document (used by gd)
set nowrap  " don't automatically wrap on load
set fo-=t   " don't automatically wrap text when typing
set colorcolumn=80
highlight ColorColumn ctermbg=233
#
" Real programmers don't use TABs but spaces
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround
set expandtab
#
" Disable stupid backup and swap files - they trigger too many events
" for file system watchers
set nobackup
set nowritebackup
set noswapfile
#
" Setup Pathogen to manage your plugins
call pathogen#infect()
#
" Settings for vim-powerline
set laststatus=2
#
" Settings for jedi-vim
let g:jedi#usages_command = "<leader>z"
let g:jedi#popup_on_dot = 0
let g:jedi#popup_select_first = 0
map <Leader>b Oimport ipdb; ipdb.set_trace() # BREAKPOINT<C-c>


