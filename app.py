
import tweepy
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import cred
import json

# Authenticate to Twitter
auth = tweepy.OAuthHandler(cred.Twitter_API_Key,  cred.Twitter_API_Secret)
auth.set_access_token(cred.Twitter_Access_Token,  cred.Twitter_Access_Secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create Twitter API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# Set Spotify scope and get authentication 
scope = 'user-read-playback-state'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.Spotify_client_ID, client_secret= cred.Spotify_client_SECRET, redirect_uri=cred.Spotify_redirect_url, scope=scope))


# Define Variables to be used in tweet 
present_name = ''
present_artist = ''
present_url = ''
prev_name = ''


# Loop which runs every 30 seconds to check if new music is playing 

from time import time, sleep
while True:
    sleep(60 - time() % 60)
    try:
        results = sp.current_playback(market='ES', additional_types=None)
        str_results = json.dumps(results)
        json_results = json.loads(str_results)

        if (json_results ["is_playing"])== True:
            # print("here")
            prev_name = present_name
            present_name = json_results ["item"]["name"]
            if (prev_name != present_name):
                present_artist = json_results ["item"]["album"]["artists"][0]["name"]
                present_url = json_results ["item"]["external_urls"]["spotify"]
                TwtStatus = "Currently playing- " + present_name +" by "+ present_artist +"! \n"+ present_url
                api.update_status(TwtStatus )
                print(TwtStatus)
                # print(present_name)
                # print(present_url)
                # print(present_artist)
            else:
                print("same song playing!")
        else:
            print ("not playing anything")
            pass
    except:
        print ("offline")
        pass




