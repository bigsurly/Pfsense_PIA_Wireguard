<!DOCTYPE html>
<html>
<head>
	<title>Pfsense_PIA_Wireguard</title>
</head>
<body>
	<h1>Pfsense_PIA_Wireguard</h1>
	<p>This script automates the recreation of a Wireguard VPN on a pfsense router.</p>
	<h3>Prerequisites:</h3>
	<ul>
		<li>Python3.8 'I think it is installed by default but if not you can type pkg install python3.8 and install from command line</li>
		<li>Curl ‘pkg install curl’ from pfsense command line</li>
		<li>Enable FreeBSD on pfsense https://docs.netgate.com/pfsense/en/latest/recipes/freebsd-pkg-repo.html</li>
		<li>Rest API for pfsense https://github.com/jaredhendrickson13/pfsense-api</li>
		<li>xmlstarlet ‘pkg install xmlstarlet’ after enabling  the full set of FreeBSD packages</li>
		<li>PIA username and password</li>
		<li>Pfsense username and password with proper permissions for the API(See API install link for more information.)</li>
		<li>SSH access on Pfsense(not required but recommended. You could also run the commands from the GUI.)</li>
	</ul>
	<p>Tested on PFSense 2.6 IF SOMETHING GOES WRONG I AM NOT LIABLE</p>
	<p>If you setup SSL with valid certificate from Let's Encrypt you can send all requests to the API over SSL.</p>
	<p>This video can show you how. <a href="https://www.youtube.com/watch?v=gVOEdt-BHDY">https://www.youtube.com/watch?v=gVOEdt-BHDY</a></p>
	<p>If you have port forward rules set on that gateway you will have to set the gateway again in the rule after the changes. I have included a sample API request for modifying a single NAT port forward rule at the end of the script. Uncomment and change accordingly to adjust the rule.</p>
	<p>1. First you need to create a dummy tunnel and peer in the Wireguard GUI in Pfsense.</p>
	<ol>
		<li>Setup the tunnel:</li>
		<ul>
			<li>Description: “Name of the Region you are connecting to”</li>
			<li>Listen Port: “any port you choose ex. 1024-65555”</li>
			<li>Private Key: fKMCeFhZ4zOncJ7GN+yFBAYtUvC2v0lghhNTGJwOutM=(This is just a placeholder)</li>
			<li>Public Key: +CGmAgeQRxGLecpGJpHnXyZugHIkZxG9Cr38Y38AK2k=(This is just a placeholder)</li>
			<li>Interface Address: 10.23.69.35/32</li>
		</ul>
		<li>Save that and create a peer.</li>
	</ol>
</body>
</html>
### Part 3: Running the Scripts

1. Connect to your pfSense router via SSH using the command `ssh root@router.ip`

2. Clone the Git repository by running `git clone https://github.com/bigsurly/Pfsense_PIA_Wireguard`

3. Change into the directory with `cd Pfsense_PIA_Wireguard`

4. Make the setup script executable by running `chmod +x setup.sh`

5. Run the setup script with `./setup.sh` and follow the prompts.

6. Once the setup is complete, run the main script with `./pia_automate.sh`.

7. If everything works correctly, you should have a working PIA VPN gateway using WireGuard in your chosen region. If you encounter any errors, delete the `config.ini` file and run the setup again, double-checking all values.

8. If you would like to monitor the gateway and have the `pia_automate.sh` script rebuild the WireGuard connection if it goes down, you can set up the `check_interfaces.py` script to run via cron. Cron can be downloaded via the standard package manager in the pfSense web GUI. You can set it up to check as often as you want.
