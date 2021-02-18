# YouTube tutorial: https://www.youtube.com/watch?v=yKz38ThJWqE&ab_channel=ImdadCodes

import requests
import time
import json
from pprint import pprint

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player'
# user-read-currently-playing token
SPOTIFY_ACCESS_TOKEN = 'BQDn5gQqr3HYE1BemCZaHI35NLItlFG354MgFSvrZSXJfnBLaaA1stO1WH7Y647jKjTIUHDqz021yUunx2BCyEpTbTtYjZueQ5t_zbT0qqIAlpve1pZRCRP5bQGALV7CM_krefwjo0im8fA2DpymGh1k'

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    resp_json = response.json()
        
    track_id = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artists_names = ', '.join( [artist['name'] for artist in artists] )
    link = resp_json['item']['external_urls']['spotify']

    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists": artists_names,
        "link": link
    }

    return current_track_info

def main():
    while True:
        current_track_info = get_current_track(
            SPOTIFY_ACCESS_TOKEN 
        )
        pprint(current_track_info, indent=4)
        time.sleep(2) # pauses every 2 seconds

if __name__ == '__main__':
    main()