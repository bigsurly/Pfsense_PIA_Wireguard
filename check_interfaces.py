import requests
import json
import time
import subprocess
import configparser
import os

# Determine the absolute path of the script
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

# Check if the configuration file exists
if not os.path.isfile(os.path.join(SCRIPT_PATH, 'config.ini')):
    print("Configuration file not found please run setup.sh first.")
    exit(1)

# Import variables from the configuration file
config = configparser.ConfigParser()
config.read(os.path.join(SCRIPT_PATH, 'config.ini'))
userpass = config.get('Default', 'userpass')
infid = config.get('Default', 'infid')
infdescr = config.get('Default', 'infdescr')
rtip = config.get('Default', 'rtip')
pfuser, pfpass = userpass.split(':')

# Call the API to check if the gateway status is online and if it changes to 'down' call the pia_automate.sh script
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
                subprocess.call([os.path.join(SCRIPT_PATH, 'pia_automate.sh')])
            print(f"Status: {status}")
            return status
        except Exception as e:
            print(f"Error parsing response: {e}")
    else:
        print(f"Request failed with status code {response.status_code}")

while True:
    response = check_status()
    if response == "online":
        break
    time.sleep(90)  # Wait for 90 seconds before making the next API call

print("Gateway is now online")