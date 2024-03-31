
import spotipy 
from spotipy import SpotifyOAuth
import streamlit as st


client_id='013dcad121c740c0bc5c0ed6a84e9ad3'

client_secret ='7900ea6ec3cd4c54a8cd1675a3ba97e5'

redirect_uri = 'http://localhost:5000'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                    client_secret= client_secret,
                                                    redirect_uri=redirect_uri,
                                                    scope="user-read-currently-playing user-read-playback-state user-read-recently-played playlist-modify-private"))


def get_recommendations(track_name):
    # Get track URI
    results = sp.search(q=track_name,type=('track','artist','genre'))
    track_uri = results['tracks']['items'][0]['uri']

    # Get recommended tracks
    recommendations = sp.recommendations(seed_tracks=[track_uri])['tracks']
    # for i in recommendations:
    #     song_link = i['external_urls']['spotify']
    #     print(song_link)
    return recommendations

st.title("Music Recommendation System")
track_name = st.text_input("Enter a song name:")


l=[]

def func():
    # sp.user_playlist_create(user='jbbijqls2jtje353lkbj4outp',name='rec songs',public=False)
    json = {'uris':l}
    sp.playlist_add_items(playlist_id='5p0UNvDA6fg4a2U6z7vVtK',items=json['uris'])
    # https://open.spotify.com/playlist/5p0UNvDA6fg4a2U6z7vVtK?si=4ad11178a0b1446b


if track_name:
    recommendations = get_recommendations(track_name)
    st.write("Recommended songs:")
    st.title('want to generate a playlist?')
    st.button('create playlist',on_click=func)
    # def add(uris):
    #     json = {'uris':[uris]}
    #     sp.playlist_add_items(playlist_id='0TniLD4zHYitd1qiiNk1lW',items=json['uris'])


    for i,track in enumerate(recommendations):
        st.write(track['name'])
        st.image(track['album']['images'][0]['url'],width=200)
        st.link_button(label='play in spotify',url=track['external_urls']['spotify'])
        l.append(track['uri'])
        
        # st.title(song)
        # st.button('add to playlist',on_click= lambda :add(uris=song),key=i)
        # st.title(track['name'])


# rec = get_recommendations('Bite me')
# for i in rec:
#     print(i['uri'])



# print(get_recommendations('hukum'))
        
# playlist = sp.user_playlist_create(user='jbbijqls2jtje353lkbj4outp',name='songs list',public=False)

# json = {"uris": ["spotify:track:6sfVSlvCl5evgokuWNrHbE"]}

# playlistsss =sp.playlist_add_items(playlist_id='3toc2pG238KrRFoZrk4SU3',items=json['uris'])



# https://open.spotify.com/playlist/3toc2pG238KrRFoZrk4SU3?si=058199ca3e9f4abb
# https://open.spotify.com/track/65zT93vcXbMxbs05YYP8dg?si=74aa05f7ad304e05
# print(playlistsss)

# spotify:track:3yOBRx27Dl7XYkEhtonb7i

# https://open.spotify.com/track/3yOBRx27Dl7XYkEhtonb7i?si=738e471b18e54204
