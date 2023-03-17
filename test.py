def read_config(file_path):
    with open(file_path) as f:
        config = {}
        for line in f:
            if line.startswith('#'):
                continue
            key, value = line.strip().split('=')
            config[key] = value
        return config

config = read_config('config.ini')
userpass = config['userpass']
print(f"userpass: {userpass}")

# use the variables in your Python code
print(f"userpass: {userpass}")
print(f"wginf: {wginf}")
print(f"wgpeer: {wgpeer}")
print(f"infid: {infid}")
print(f"infdescr: {infdescr}")
print(f"rtip: {rtip}")
print(f"gateid: {gateid}")
print(f"py: {py}")
print(f"piausername: {piausername}")
print(f"piapassword: {piapassword}")
print(f"piaregion: {piaregion}")