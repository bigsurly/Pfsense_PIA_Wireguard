import configparser
import os
from pathlib import Path

# Determine the absolute path of the script
SCRIPT_PATH = str(Path(__file__).resolve().parent)

# Check if the configuration file exists
if not os.path.isfile(f'{SCRIPT_PATH}/config.ini'):
    print("Configuration file not found, please run setup.sh first.")
    exit(1)

# Import variables from the configuration file
config = configparser.ConfigParser()
config.read(f'{SCRIPT_PATH}/config.ini')

userpass = config.get('Default', 'userpass')
wginf = config.get('Default', 'wginf')
wgpeer = config.get('Default', 'wgpeer')
infid = config.get('Default', 'infid')
infdescr = config.get('Default', 'infdescr')
rtip = config.get('Default', 'rtip')
gateid = config.get('Default', 'gateid')
py = config.get('Default', 'py')
piausername = config.get('Default', 'piausername')
piapassword = config.get('Default', 'piapassword')
piaregion = config.get('Default', 'piaregion')

from piawg import piawg
from pick import pick
from getpass import getpass
from datetime import datetime

pia = piawg()

# Generate public and private key pair
pia.generate_keys()

# Set PIA region
region = piaregion
pia.set_region(region)

# Get token
while True:
    if pia.get_token(piausername, piapassword):
        print("Login successful!")
        break
    else:
        print("Error logging in, please try again...")

# Add key
status, response = pia.addkey()
if status:
    print("Added key to server!")
else:
    print("Error adding key to server")
    print(response)

# Build config
timestamp = int(datetime.now().timestamp())
location = pia.region.replace(' ', '-')
config_file = f"PIA-{location}-{timestamp}.conf"
print(f"Saving configuration file {config_file}")
with open(f"{SCRIPT_PATH}/{config_file}", "w") as file:
    file.write("[Interface]\n")
    file.write(f"Address = {pia.connection['peer_ip']}\n")
    file.write(f"PrivateKey = {pia.privatekey}\n")
    file.write(f"DNS = {pia.connection['dns_servers'][0]},{pia.connection['dns_servers'][1]}\n\n")
    file.write("[Peer]\n")
    file.write(f"PublicKey = {pia.connection['server_key']}\n")
    file.write(f"Endpoint = {pia.connection['server_ip']}:1337\n")
    file.write("AllowedIPs = 0.0.0.0/0\n")
    file.write("PersistentKeepalive = 25\n")