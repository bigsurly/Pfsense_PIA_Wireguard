import configparser

config = configparser.ConfigParser()
config.read('config.ini')

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

#Set PIA region
#Set PIA region
region = piaregion
pia.set_region(region)

# Get token
while True:
    #username = piausername
    #password = piapassword
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
config_file = 'PIA-{}-{}.conf'.format(location, timestamp)
print("Saving configuration file {}".format(config_file))
with open(config_file, 'w') as file:
    file.write('[Interface]\n')
    file.write('Address = {}\n'.format(pia.connection['peer_ip']))
    file.write('PrivateKey = {}\n'.format(pia.privatekey))
    file.write('DNS = {},{}\n\n'.format(pia.connection['dns_servers'][0], pia.connection['dns_servers'][1]))
    file.write('[Peer]\n')
    file.write('PublicKey = {}\n'.format(pia.connection['server_key']))
    file.write('Endpoint = {}:1337\n'.format(pia.connection['server_ip']))
    file.write('AllowedIPs = 0.0.0.0/0\n')
    file.write('PersistentKeepalive = 25\n')
