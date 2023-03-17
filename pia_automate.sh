#!/bin/sh

# Import variables from the configuration file
. ./config.ini

#Make sure there are not config files already present
rm wg1.conf
find . -name "PIA*.conf" -exec rm '{}' \;

#Generate config file
$py generate-config.py
#echo "Chill out!"
sleep 5
echo "OK Proceeding!"

#Rename generated PIA config file
find . -name "PIA*.conf" -exec cp '{}' wg1.conf \;
#Delete original conf file
find . -name "PIA*.conf" -exec rm '{}' \;

#Parse data from the new conf file wg1.conf
newinfaddr=$(awk '/^Address/{print $3}' wg1.conf)
privkey=$(awk '/^PrivateKey/{print $3}' wg1.conf)
remotepubkey=$(awk '/^PublicKey/{print $3}' wg1.conf)
endpoint=$(awk '/^Endpoint/{print $3}' wg1.conf)
fixedendpoint=$(echo $endpoint | sed 's/:1337//g')

#Generate new public key from private key
pubkey=$(echo $privkey | wg pubkey)

#echo parsed data omiting the private key
echo "New Interface Address: $newinfaddr"
echo "New Public Key: $pubkey"
echo "New Endpoint: $fixedendpoint"

#remove PIA conf file becuase we are done with it
rm wg1.conf

#add new keys to pfsense config.xml
xml ed --inplace -u "/pfsense/installedpackages/wireguard/tunnels/item[name='$wginf']/privatekey" --value "$privkey" /conf/config.xml
xml ed --inplace -u "/pfsense/installedpackages/wireguard/tunnels/item[name='$wginf']/publickey" --value "$pubkey" /conf/config.xml
xml ed --inplace -u "/pfsense/installedpackages/wireguard/peers/item[descr='$wgpeer']/publickey" --value "$remotepubkey" /conf/config.xml
xml ed --inplace -u "/pfsense/installedpackages/wireguard/peers/item[descr='$wgpeer']/endpoint" --value "$fixedendpoint" /conf/config.xml

#Remove cached config
rm /tmp/config.cache

#Update the gateway
curl -u $userpass -H "Content-Type: application/json" -d '{"id": "'$gateid'", "gateway": "'$newinfaddr'"}' -X PUT $rtip/api/v1/routing/gateway

#Remove the old interface
curl -u $userpass -H "Content-Type: application/json" -d '{"if":"'$wginf'"}' -X DELETE $rtip/api/v1/interface
#echo "Chill out!"
sleep 5
echo "OK Proceeding!"

#Add the new modified interface
curl -u $userpass -H "Content-Type: application/json" -d '{"id":"'$infid'","descr":"'$infdescr'","if":"'$wginf'","ipaddr": "'$newinfaddr'","subnet":32,"enable":true,"type":"staticv4","mss":1380}' -X POST $rtip/api/v1/interface
#echo "Chill out!"
sleep 5
echo "OK Proceeding!"

#Apply the changes
curl -u $userpass -H "Content-Type: application/json" -X POST $rtip/api/v1/interface/apply

#Apply the changes to the gateway
curl -u $userpass -H "Content-Type: application/json" -X POST $rtip/api/v1/routing/apply

#restart wireguard service
curl -u $userpass -H "Content-Type: application/json" -d '{"service": "wireguard"}' -X POST $rtip/api/v1/services/restart
#echo "Chill out!"
sleep 5
echo "OK Proceeding!"

#Update NAT port forward rule for Plex over PIA VPN - it breaks after all the changes and revers to WAN gateway
#curl -u $userpass -H "Content-Type: application/json" -d '{"id":"0", "interface": "'$infid'"}' -X PUT $rtip/api/v1/firewall/nat/port_forward
##Apply the changes
#curl -u $userpass -H "Content-Type: application/json"  -X POST $rtip/api/v1/firewall/apply

echo "Holy crap it worked."
