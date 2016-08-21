#Standar Imports
import getpass
# Custom Imports


WELCOME = """
   _____  _    _  _______   ____
  |  _  || |  | ||__   __| / __ \\
  | |_| || |  | |   | |   | |  | |
  |  _  || |__| |   | |   | |__| |
  |_| |_||______|   |_|    \____/
         _____  ___    _  _____  _______  _____  _      _
        |_   _||   \  | || ____||__   __||  _  || |    | |
          | |  | |\ \ | |\___  \   | |   | |_| || |    | |
         _| |_ | | \ \| | ___| |   | |   |  _  || |___ | |___
        |_____||_|  \___||_____/   |_|   |_| |_||_____||_____|

Hi "{}", welcome to the autoinstall script!

You need to run this as administrator (sudo).

You will also need a working internet connection, so if you have not done so already, please configure your internet connection.

(Messages will be saved into logfile on '.log/autoinstall.log')

""".format(getpass.getuser())

ROOT_ERROR = """
You have to run this as sudo.
"""
MESSAGES = {'welcome':WELCOME, 'root_error':ROOT_ERROR}
