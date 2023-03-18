#!/bin/sh

# Determine the absolute path of the script
SCRIPT_PATH=$(dirname "$(readlink -f "$0")")

# Prompt user for input and store in variables
echo "Please select a region from the list below: "
python3.8 ${SCRIPT_PATH}/regions.py
read -p "Enter your selected region: " piaregion

read -p "Enter Pfsense username and password(ex. admin:password): " pfsense_username
read -p "Enter the name of your wireguard interface(ex. tun_wg1): " wireinf
read -p "Enter the name of the Wireguard peer you setup: " wirepeer
read -p "Enter the interface id of the interface you created(ex. opt1,opt,opt3): " interfaceid
read -p "Enter the interface description(ex. Atlanta): " intdescription 
read -p "Enter your router's IP or URL: " rtip
read -p "Enter your gateway ID (0 for WAN1, 1 for WAN2, etc.): " gateid
read -p "Enter your PIA username: " piausername
read -p "Enter your PIA password: " piapassword
# Set default value
default_python="python3.8"
# Prompt user for input or use default value
echo -n "Enter your Python command or hit enter for default ($default_python): "
read python_command
python_command=${python_command:-$default_python}

# Write variables to config.ini file
echo "[Default]" > ${SCRIPT_PATH}/config.ini
echo "userpass=$pfsense_username" >> ${SCRIPT_PATH}/config.ini
echo "wginf=$wireinf" >> ${SCRIPT_PATH}/config.ini
echo "wgpeer=$wirepeer" >> ${SCRIPT_PATH}/config.ini
echo "infid=$interfaceid" >> ${SCRIPT_PATH}/config.ini
echo "infdescr=$intdescription" >> ${SCRIPT_PATH}/config.ini
echo "rtip=$rtip" >> ${SCRIPT_PATH}/config.ini
echo "gateid=$gateid" >> ${SCRIPT_PATH}/config.ini
echo "py=$python_command" >> ${SCRIPT_PATH}/config.ini
echo "piausername=$piausername" >> ${SCRIPT_PATH}/config.ini
echo "piapassword=$piapassword" >> ${SCRIPT_PATH}/config.ini
echo "piaregion=$piaregion" >> ${SCRIPT_PATH}/config.ini

#Make pia_automate executable
chmod +x ${SCRIPT_PATH}/pia_automate.sh
chmod +x ${SCRIPT_PATH}/check_interface.py

echo "Config file setup completed!"