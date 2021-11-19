# Patrick Sacchet
# Version 1.1
# File implements soundcloud interaction and playing functionality
# NOTE: Not yet integrated into main - TODO

# Please note this API is deprecated... sadly... but it still works?
import soundcloud

client = soundcloud.Client(client_id=YOUR_CLIENT_ID)

tracks = client.get('/tracks', limit=10)
for track in tracks.collection:
    print track.title
app = client.get('/apps/124')
print app.permalink_url
