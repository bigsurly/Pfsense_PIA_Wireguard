<h1>Pfsense_PIA_Wireguard</h1>
<p>This script automates the recreation of a Wireguard VPN on a pfsense router.</p>
<h2>Prerequisites</h2>
<ul>
	<li>Python 3.8 (If not installed, run pkg install python3.8 from the command line.)</li>
	<li>Curl (Run `pkg install curl` from the pfsense command line.)</li>
	<li>Enable FreeBSD on Pfsense (Refer to the <a href="https://docs.netgate.com/pfsense/en/latest/recipes/freebsd-pkg-repo.html">official documentation</a>.)</li>
	<li>Rest API for Pfsense (Install from <a href="https://github.com/jaredhendrickson13/pfsense-api">https://github.com/jaredhendrickson13/pfsense-api</a>.)</li>
	<li>Xmlstarlet (Run pkg install xmlstarlet after enabling the full set of FreeBSD packages.)</li>
	<li>PIA username and password</li>
	<li>Pfsense username and password with proper permissions for the API (See API install link for more information.)</li>
	<li>SSH access on Pfsense (Not required but recommended. You could also run the commands from the GUI.)</li>
</ul>

<p>Note: This script has been tested on PFSense 2.6. If something goes wrong, the author is not liable.</p>

<h2>Setup Instructions</h2>
<p>If you set up SSL with a valid certificate from Let's Encrypt, you can send all requests to the API over SSL. Refer to this <a href="https://www.youtube.com/watch?v=gVOEdt-BHDY">video</a> for more information.</p>

<p>If you have port forward rules set on that gateway, you will have to set the gateway again in the rule after the changes. I have included a sample API request for modifying a single NAT port forward rule at the end of the script. Uncomment and change accordingly to adjust the rule.</p>

1.	Create a dummy tunnel and peer in the Wireguard GUI in Pfsense.
		Setup the tunnel
			
			Description: "Name of the Region you are connecting to"
			Listen Port: "any port you choose ex. 1024-65555"
			Private Key: fKMCeFhZ4zOncJ7GN+yFBAYtUvC2v0lghhNTGJwOutM= (This is just a placeholder)
			Public Key: +CGmAgeQRxGLecpGJpHnXyZugHIkZxG9Cr38Y38AK2k= (This is just a placeholder)
			Interface Address: 10.23.69.35/32
	Save that and create a peer.

2.	Assign the peer to the newly created tunnel. To find the name, go back to the main tunnels screen and you will see something like tun_wg0 or tun_wg1, which is the name of your Wireguard interface.
		Setup the Peer
			
			Tunnel: "Select the tunnel you just set up"
			Description: "This is the name of the endpoint and also the $wgpeer variable"
			Endpoint: "Any IP address is fine, this is just a placeholder ex. 1.1.1.1"
			Keep Alive: 25
			Public Key: "Vam3XRk6jA6+R5PwTY4C5Xzwa/EjR9u1T0ynpawvlEc=" (This is also just a placeholder)

3.	Go to interface assignments and assign the new tunnel to an interface and set the IPV4 type to static.
		Set the IP to 10.129.246.23/32 (or any IP this is just a placeholder) and save.

4.	Go to System>Routing and add a gateway

			Interface: "The Inteface we just made"
			Gateway: 10.23.69.1 (This is just a placeholder)
			Address Family:IPv4
			Name:"Whatever you want"
			Monitor IP: 10.0.0.242
	Save and apply


1. Connect to your pfSense router via SSH using the command `ssh root@router.ip`

2. Clone the Git repository by running `git clone https://github.com/bigsurly/Pfsense_PIA_Wireguard`

3. Change into the directory with `cd Pfsense_PIA_Wireguard`

4. Make the setup script executable by running `chmod +x setup.sh`

5. Run the setup script with `./setup.sh` and follow the prompts.

6. Once the setup is complete, run the main script with `./pia_automate.sh`.

7. If everything works correctly, you should have a working PIA VPN gateway using WireGuard in your chosen region. If you encounter any errors, delete the `config.ini` file and run the setup again, double-checking all values.

8. If you would like to monitor the gateway and have the `pia_automate.sh` script rebuild the WireGuard connection if it goes down, you can set up the `check_interfaces.py` script to run via cron. Cron can be downloaded via the standard package manager in the pfSense web GUI. You can set it up to check as often as you want.
