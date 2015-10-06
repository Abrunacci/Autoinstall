#!/bin/bash
atp-get update
apt-get upgrade

# SUDO
apt-get -y install sudo
adduser $USERNAME sudo

# Tools
apt-get install -y curl python-pip flashplugin-nonfree openjdk-7-jdk gparted git

# Administrador de archivos
apt-get  install -y nemo

# Procesador de texto
apt-get install -y vim-nox

# Terminal
apt-get install -y terminator
apt-get install -y zsh
chsh -s $(which zsh)

# SQL
apt-get install -y postgresql9.4
apt-get install -y postgresql-contrib 
apt-get install -y postgresql-server-dev-all
apt-get install -y pgadmin3
vim /etc/postgresql/9.4/main/pg_hba.conf
vim /etc/postgresql/9.4/main/postgresql.conf

# Dev
apt-get install -y python-dev idle

# Media
apt-get install -y vlc

# Torrent 
apt-get install -y transmission

# Virtualization
apt-get install -y linux-headers-$(uname -r|sed 's,[^-]*-[^-]*-,,') virtualbox
adduser $USERNAME vboxusers


# oh-my-zsh
sudo -u $USERNAME sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# syntax highlighting for oh-my-zsh
git clone git://github.com/zsh-users/zsh-syntax-highlighting.git 
mv zsh-syntax-highlighting /home/$USERNAME/.oh-my-zsh/plugins/

sed -i '1i source /home/'$USERNAME'/.oh-my-zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh' /home/$USERNAME/.zshrc
sudo vim /home/$USERNAME/.zshrc

# venv
pip install virtualenvwrapper

sed -i '1i export WORKON_HOME=$HOME/.virtualenvs' /home/$USERNAME/.zshrc
sed -i '2i export MSYS_HOME=/c/msys/1.0' /home/$USERNAME/.zshrc


# VIM AS PYTHON IDE
git clone https://github.com/mbrochh/vim-as-a-python-ide.git
mv vim-as-a-python-ide/.vimrc /home/$USERNAME/
rm -rf vim-as-a-python-ide
sudo -u $USERNAME mkdir /home/$USERNAME/.vim
sudo -u $USERNAME mkdir /home/$USERNAME/.vim/colors
sudo -u $USERNAME mkdir /home/$USERNAME/.vim/autoload
sudo -u $USERNAME mkdir /home/$USERNAME/.vim/bundle
git clone git://github.com/Lokaltog/vim-powerline.git
git clone git://github.com/davidhalter/jedi-vim.git
mv vim-powerline jedi-vim /home/$USERNAME/.vim/bundle/
wget -O wombat256mod.vim "http://www.vim.org/scripts/download_script.php?src_id=13400"
mv wombat256mod.vim /home/$USERNAME/.vim/colors/ 
curl -so /home/$USERNAME/.vim/autoload/pathogen.vim "https://raw.githubusercontent.com/tpope/vim-pathogen/master/autoload/pathogen.vim"
chown -R $USERNAME /home/$USERNAME/.vim

vim /home/$USERNAME/.vimrc

echo '***********************'
echo '      FINALIZADO       '
echo '***********************'

