# Pfsense_PIA_Wireguard
This scripts automates the recreation of a Wireguard VPN on a pfsense router.

Prequisites
-Python3.8 
-Curl ‘pkg install curl’ from pfsense command line
-Enable FreeBSD on pfsense https://docs.netgate.com/pfsense/en/latest/recipes/freebsd-pkg-repo.html
-Rest API for pfsense https://github.com/jaredhendrickson13/pfsense-api
-xmlstarlet ‘pkg install xmlstarlet’ after enabling  the full set of FreeBSD packages
-PIA username and password

Tested on PFSense 2.6

If you setup ssl with valid certificates on pfense you can encrypt all requests to the api

If you have port forward rules set on that gateway you will have to set the gateway again in the rule after the changes.  I have included a sample API request for modifying a single rule

	-This can be done by following the instructions in this video How To Setup ACME, Let's Encrypt, and HAProxy HTTPS ...

First you need to create a dummy tunnel and peer in the wireguard gui in pfsense.  

Setup the tunnel:

Description: “Name of the Region you are connecting to”
Listen Port: “any port you choose ex. 1024-65555”
Private Key:fKMCeFhZ4zOncJ7GN+yFBAYtUvC2v0lghhNTGJwOutM=(This is just a placeholder)
Public Key: +CGmAgeQRxGLecpGJpHnXyZugHIkZxG9Cr38Y38AK2k=(This is just a placeholder)
Interface Address: 10.23.69.35/32
 
Save that and create the a peer

Assign the peer to the newly created tunnel.  To find the name go back to the main tunnels screen and you will see something like tun_wg0 or tun_wg1, that is the name of you wireguard interface.

Setup the Peer

Tunnel: "Select the tunnel you jus setup"
Description: "This is the name of the endpoint and also the $wgpeer variable"
Endpoint: "Any IP address is fine, this is just a placeholder ex. 1.1.1.1"
Keep Alive: 25
Public Key: "Vam3XRk6jA6+R5PwTY4C5Xzwa/EjR9u1T0ynpawvlEc=" (This is also just a placeholder)
	