from piawg import piawg
from pick import pick
from getpass import getpass
from datetime import datetime

pia = piawg()

# Generate public and private key pair
pia.generate_keys()

# Select region
title = 'Please choose a region: '
options = sorted(list(pia.server_list.keys()))
option, index = pick(options, title)
pia.set_region(option)
print("Selected '{}'".format(option))
