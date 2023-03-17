#!/bin/sh

# Prompt user for input and store in variables
echo "Please select a region from the list below: "
python3.8 regions.py
read -p "Enter your selected region: " piaregion

read -p "Enter Pfsense username and password(ex. admin:password): " pfsense_username
read -p "Enter the name of your wireguard interface(ex. tun_wg1): " wireinf
read -p "Enter the name of the Wireguard peer you setup: " wirepeer
read -p "Enter the interface id of the interface you created(ex. opt1,opt,opt3): " interfaceid
read -p "Enter the interface description(ex. Atlanta): " intdescription 
read -p "Enter your router's IP or URL: " rtip
read -p "Enter your gateway ID (0 for WAN1, 1 for WAN2, etc.): " gateid
#read -e -i "python3.8" -p "Enter your Python command or hit enter for default Python3.8: " py
read -p "Enter your PIA username: " piausername
read -p "Enter your PIA password: " piapassword
# Set default value
default_python="python3.8"
# Prompt user for input or use default value
echo -n "Enter your Python command or hit enter for default ($default_python): "
read python_command
python_command=${python_command:-$default_python}

# Write variables to config.ini file
echo "[DEFAULT]" > config.ini
echo "userpass=$pfsense_username" >> config.ini
echo "wginf=$wireinf" >> config.ini
echo "wgpeer=$wirepeer" >> config.ini
echo "infid=$interfaceid" >> config.ini
echo "infdescr=$intdescription" >> config.ini
echo "rtip=$rtip" >> config.ini
echo "gateid=$gateid" >> config.ini
echo "py=$python_command" >> config.ini
echo "piausername=$piausername" >> config.ini
echo "piapassword=$piapassword" >> config.ini
echo "piaregion=$piaregion" >> config.ini

chmod +x pia_automate.sh

echo "Config file setup completed!"