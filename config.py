
APPLICATIONS = [
    'curl',
    'python-pip',
    'git',
    'vim-nox',
    'virtualbox',
    'flashplugin-nonfree',
    'openjdk-7-jdk',
    'blueman',
    'gparted',
    'terminator',
    'python-dev',
    'python3-dev',
    'idle',
    'vlc',
    'transmission',
    'virtualenvwrapper',
    'zsh',
    'keepassx',
    'ssh',
    'apt-transport-https',
    'owncloud-client',
    'meld',
]



"""
 If one application need to execute some configuration we set it right here
 key: name of application, value: list of commands
"""
ADDITIONAL_COMMANDS = {
    'virtualbox': ['adduser $USERNAME vboxusers', ],
}
