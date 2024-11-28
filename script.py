import spotipy
from spotipy.oauth2 import SpotifyOAuth

# read identification file 
file = open("ids.txt", "r") 
id_lines = file.readlines()
for i in range(len(id_lines)): 
    id_lines[i] = id_lines[i].strip('\n')
file.close()

# read volumes file
file = open("volumes.txt", "r") 
vol_lines = file.readlines()
for i in range(len(vol_lines)): 
    vol_lines[i] = vol_lines[i].strip('\n')
file.close()

# find next volume to change to 
vols = vol_lines[0].split(' ')
index = vols.index(vol_lines[1])
index = index + 1 if index + 1 < len(vols) else 0
new_vol = int(vols[index])

# save data to volume file 
file_str = "" 
for vol in vols:
    file_str += vol
    file_str += " "
file_str = file_str[:-1]
file_str += ('\n' + vols[index])
file = open("volumes.txt", "w") 
file.write(file_str)
file.close()

# create authentication manager 
redirect_uri = "http://localhost:7000/callback"
scope = "user-modify-playback-state"
auth_manager = SpotifyOAuth(client_id=id_lines[0], client_secret=id_lines[1], redirect_uri=redirect_uri, scope=scope)

# set volume of spotify
spotify = spotipy.Spotify(auth_manager=auth_manager)
spotify.volume(volume_percent=new_vol)
