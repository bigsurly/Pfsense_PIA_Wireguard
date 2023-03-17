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

Setup the peer like this
	