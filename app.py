import tweepy
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import cred
import json
from time import  sleep
from datetime import datetime
logfile = open("logs.txt", "a") 

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
api = tweepy.API(auth)


# Set Spotify scope and get authentication 
scope = 'user-read-playback-state'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.Spotify_client_ID, client_secret= cred.Spotify_client_SECRET, redirect_uri=cred.Spotify_redirect_url, scope=scope))


# Define Variables to be used in tweet 
present_name = ''
present_artist = ''
present_url = ''
prev_url = ''


# Loop which runs every 30 seconds to check if new music is playing 

while True:
    sleep(30)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    try:
        results = sp.current_playback(market='ES', additional_types=None)
        str_results = json.dumps(results)
        json_results = json.loads(str_results)
        if (json_results ["is_playing"])== True:
            # print("here")
            prev_url = present_url 
            present_url = json_results ["item"]["external_urls"]["spotify"]
            if (prev_url != present_url ):
                present_artist = json_results ["item"]["artists"][0]["name"]
                present_name = json_results ["item"]["name"]
                TwtStatus =  " Currently playing- " + present_name +" by "+ present_artist +"! \n"+ present_url
                api.update_status(current_time + TwtStatus )
                print(TwtStatus)
                logfile.write(current_time +" " + present_name + "  "+ present_artist + "\n")
            else:
                print("same song playing!")
                logfile.write(current_time+ " same song playing!"+ "\n")
        else:
            print ("not playing anything")
            logfile.write(current_time+ " not playing anything"+ "\n")
    except Exception as e:
        print ("error "+ str(e))
        logfile.write(current_time+ "error "+ str(e)+ "\n")
