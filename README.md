# Pfsense_PIA_Wireguard
This scripts automates the recreation of a Wireguard VPN on a pfsense router. I plan to link this with a cron script that pings out the PIA gateway and fires this script when the ping fails.

Prequisites
-Python3.8 'I think it is installed by default but if not you can type pkg install python3.8 and install from command line
-Curl ‘pkg install curl’ from pfsense command line
-Enable FreeBSD on pfsense https://docs.netgate.com/pfsense/en/latest/recipes/freebsd-pkg-repo.html
-Rest API for pfsense https://github.com/jaredhendrickson13/pfsense-api
-xmlstarlet ‘pkg install xmlstarlet’ after enabling  the full set of FreeBSD packages
-PIA username and password
-Pfsnse username and password with proper permissions for the API(See API install link for more information.)
-SSH access on Pfsense(not required but reccomended.  You could also run the commands from the gui.)

Tested on PFSense 2.6 IF SOMETHING GOES WRONG I AM NOT LIABLE

If you setup ssl with valid certificate from Let's Encrypt you can send all requests to the API over SSL. 

This video can show you how.   https://www.youtube.com/watch?v=gVOEdt-BHDY

If you have port forward rules set on that gateway you will have to set the gateway again in the rule after the changes.  I have included a sample API request for modifying a single NAT port forward rule at the end of the script.  Uncomment and change accordingly to adjust the rule.


1.	First you need to create a dummy tunnel and peer in the wireguard gui in pfsense.  

		Setup the tunnel:

				Description: “Name of the Region you are connecting to”
				Listen Port: “any port you choose ex. 1024-65555”
				Private Key:fKMCeFhZ4zOncJ7GN+yFBAYtUvC2v0lghhNTGJwOutM=(This is just a placeholder)
				Public Key: +CGmAgeQRxGLecpGJpHnXyZugHIkZxG9Cr38Y38AK2k=(This is just a placeholder)
				Interface Address: 10.23.69.35/32
 
		Save that and create a peer.

2. Assign the peer to the newly created tunnel.  To find the name go back to the main tunnels screen and you will see something like tun_wg0 or tun_wg1, that is the name of you wireguard interface.

		Setup the Peer:

				Tunnel: "Select the tunnel you jus setup"
				Description: "This is the name of the endpoint and also the $wgpeer variable"
				Endpoint: "Any IP address is fine, this is just a placeholder ex. 1.1.1.1"
				Keep Alive: 25
				Public Key: "Vam3XRk6jA6+R5PwTY4C5Xzwa/EjR9u1T0ynpawvlEc=" (This is also just a placeholder)


3.	Go to interface assignments and assing the new tunnel to an interface and set the IPV4 type to static.

		set the ip to 10.129.246.23/32(or any ip as this is just a placeholder) and save.

4.	Go to System>Routing and add a gateway

				Interface: "The Inteface we just made"
				Gateway: 10.23.69.1 (This is just a placeholder)
				Address Family: IPv4
				Name:"Whatever you want"
				Monitor IP: 10.0.0.242

				Save and apply

5.  Go login to the router via ssh 'ssh root@router.ip'

6. Git clone the repo 'git clone https://github.com/bigsurly/Pfsense_PIA_Wireguard'

7.	cd into the directory 'cd Pfsense_PIA_Wireguard'

8. run the setup 
		'chmod setup.sh'
		'./setup.sh'

9. Onc setup is complete you can run the script.
		'./pia_automate.sh'

7.  If everything works you should have a working PIA VPN gateway using Wireguard in your chosen region.  If you get errors delete the config.ini file and run setup again, making sure to double check all values.








	