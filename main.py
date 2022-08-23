#we create billboard to spotify app

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from extractor import songs_dict,date

print(songs_dict)




spotify_auth = spotipy.oauth2.SpotifyOAuth(client_id="613bd93cece64f059c832ab8816bf082",
                                           client_secret="c85f3c04fa794f32bdddda653aab1bb8",
                                           redirect_uri="http://example.com",
                                           scope="playlist-modify-private",
                                           cache_path="token.txt")

sp = spotipy.Spotify(auth_manager=spotify_auth)
user_id = user_id = sp.current_user()["id"]
found_soungs = []
songs_ur = []
for i in range(1,len(songs_dict.keys())):



    results = sp.search(q=songs_dict[str(i)], limit=1)
    uri = results["tracks"]['items'][0]['uri']
    
    songs_ur.append(uri)
print(songs_ur)
    # for idx, track in enumerate(results['tracks']['items'][0]['uri'],1):
    #     print(idx, track['name'])
    #     found_soungs.append(track['name'])
    # print(found_soungs)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist['id'], items=songs_ur)

