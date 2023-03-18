import requests
import json
import time
import subprocess
import configparser
import os

# Check if the configuration file exists
if not os.path.isfile('./config.ini'):
    print("Configuration file not found please run setup.sh first.")
    exit(1)

# Import variables from the configuration file
with open('./config.ini', 'r') as f:
    for line in f:
        # Process each line in the config file
        ...
config = configparser.ConfigParser()
config.read('config.ini')
userpass = config.get('Default', 'userpass')
infid = config.get('Default', 'infid')
infdescr = config.get('Default', 'infdescr')
rtip = config.get('Default', 'rtip')
pfuser, pfpass = userpass.split(':')

#Call the API to check if the gatewasy status is online and if it changes to down call the pia_automate.sh script
def check_status():
    url = f"{rtip}/api/v1/status/gateway"
    headers = {"Content-Type": "application/json"}
    data = {"name": infdescr}
    response = requests.get(url, headers=headers, auth=(pfuser, pfpass), json=data)
    if response.status_code == 200:
        try:
            response_json = json.loads(response.text)
            status = response_json['data'][0]['status']
            if status == 'down':
                subprocess.call(['./pia_automate.sh'])
            print(f"Status: {status}")
        except Exception as e:
            print(f"Error parsing response: {e}")
    else:
        print(f"Request failed with status code {response.status_code}")

while True:
    check_status()
    time.sleep(60)
    if status == 'online':
        print("Gateway status is online. Exiting the loop.")
        break