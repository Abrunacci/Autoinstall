# AUTOINSTALL Customization

## What is this ?

This script was created to facilitate the post-installation "Debian Jessie".

## What this does?

When "./Autoinstall.sh" is executed, the scritp begins to perform actions as follows:

* Update and upgrade the system.
* Add sudoers to sudo group.
* Install prerequisites (git, python-pip and configParser).
* Run autoinstall.py.

Once "autoinstall.py" is running, the "APPLICATIONS.INI" file is read and starts with the installation of all applications that are there.

## How to add applications?

To add an application in the 'APPLICATIONS.INI' file should do as follows:

[application's name]<br>
install: True

If the applications have prerequisites you only have to add in section the 'prerequisites' option

[application's name]<br>
install: True<br>
prerequisites: prerequisite1, prerequisite2, prerequisite3<br>


If you want to install related packages (ex: postgresql -> postgresql-contrib):

[application's name]<br>
install: True<br>
prerequisites: prerequisite1, prerequisite2, prerequisite3<br>
related_packages: other_application, other_application2<br>

If the application requires edit a config file just add the option path:

[application's name]<br>
install: True<br>
prerequisites: prerequisite1, prerequisite2, prerequisite3<br>
related_packages: other_application, other_application2<br>
path: "path1", "path2"<br>

If the application requires other commands after installation (ex: add user to group)

[application's name]<br>
install: True<br>
prerequisites: prerequisite1, prerequisite2, prerequisite3<br>
related_packages: other_application, other_application2<br>
path: "path1", "path2"<br>
other_commands: command1, command2, command3




