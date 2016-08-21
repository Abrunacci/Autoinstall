# Autoinstall
> Python script to complete Debian installations.

## Execution

Linux:

```sh
sudo ./run.py
```

## Usage example

This script is designed based on a common problem when migrating between Debian distributions.
It all starts with a question: What had installed in my previous distribution?

To solve this problem that arose when migrating between LMDE, Debian, Crunchbangs (now Bunsenlabs) and other Debian-based distributions, I happened to create a script that loops through a list of applications and libraries and will automatically installing (something like a requirements.txt, but with apps)

That's how we got here.

In the file config.py we have 2 variables, one APPLICATIONS call and the other ADDITIONAL_COMMANDS:

APPLICATIONS has the following format:

```
APPLICATIONS = [ 'application_name', 'application_name']
```

ADDITIONAL_COMMANDS has the following format:

```
ADDITIONAL_COMMANDS = { 'application_name': [ 'TERMINAL_COMMAND']}
```


APPLICATIONS is required to run the script.

ADDITIONAL_COMMANDS should only be completed if needed. For example, when installing 'virtualbox' we should add our user to vboxusers group then becomes:

ADDITIONAL_COMMANDS = { 'virtualbox': [ 'adduser $ USERNAME vboxusers']}


## Development setup

There is no need to setup. All the imports MUST BE standard

```sh
git clone https://github.com/Abrunacci/Autoinstall
cd Autoinstall
git checkout develop
```

## Release History

* 0.1.0
    * RELEASE:
      * autoinstall.py
      * config.py
      * log.py
* 0.1.1
    * Work in progress:
      * Add console customization (oh my zsh)
      * Add UPDATE and UPGRADE repositories.


## Meta

Alejandro Brunacci – [@Abrunacci87](https://twitter.com/Abrunacci87) – Abrunacci@Bitson.com.ar

Distributed under the GPL3 license. See ``LICENSE`` for more information.

[https://github.com/abrunacci](https://github.com/Abrunacci/)
