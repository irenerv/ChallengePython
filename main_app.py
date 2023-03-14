import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

#Loading environmental variables
load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

#Authenticate to spotify service
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

# Show most common songs of an artist
artist = str(input("What top 10 artist would you like to see: ")).lower()
results = sp.search(q=artist, limit=10)
top = 0

# Show top ten songs
for track in results['tracks']['items']:
    top+=1
    print(('#'+str(top) + '- ' + track['name']).ljust(34)+'** '+ str(track['popularity']) + '/100')

#Save songs
preferred_songs = []
keep = True
while(len(preferred_songs) < 2 or keep):
    decision = str(input("\nWould you like to save a song?: (Yes/No)")).lower()
    if(decision == 'yes'):
        top_id = 0
        while(top_id <= 0 or top_id > 10 ):
            top_id = int(input("From 1 to 10, which top ten song do you want?"))
        preferred_songs.append({"top_song" : top_id, 
                                "name": results['tracks']['items'][top_id-1]['name'],
                                "popularity": results['tracks']['items'][top_id-1]['popularity'],
                                "duration": (results['tracks']['items'][top_id-1]['duration_ms']/1000)/60})
    else:
        if len(preferred_songs) >= 2:
            keep = False

#Show list of saved songs
total_duration=0
for song in preferred_songs:
    print(('#'+ str(song['top_song']) + '- ' + song['name']).ljust(40)+'** '+ str(song['popularity']) + '/100')
    total_duration+=song['duration']
print('\nTotal playlist duration: ' + str(round(total_duration, 2)) + ' min.')




