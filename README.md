# Spoitfy_Twitter_Bot

A bot which tweets the song I'm currently listening to on spotify!

## Dependancies 

1. [Spotipy](https://spotipy.readthedocs.io/en/2.18.0/)
2. [Tweepy](https://www.tweepy.org/)

## Run it yourself

1. Clone the repo first and install the dependancies uisng `py -m pip install -r requirements.txt`
2. Add a file called `cred.py` in the home directory and add in you Twitter and Spotify developer API keys in the following format -
 ```python
Twitter_API_Key= #Your Twitter API Key 
Twitter_API_Secret= #Your Twitter Secret API Key 
Twitter_Access_Token= #Your Twitter Access Token
Twitter_Access_Secret= #Your Twitter Secret Access Token 

Spotify_client_ID= #Your Spotify Client ID
Spotify_client_SECRET= #Your Spotify Client Secret 
Spotify_redirect_url= 'http://localhost:3000/'  #Make sure you add in this http address into your spotify developer app settings
 ```
3. Run `python app.py` :)


testtest123

