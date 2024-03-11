from googleapiclient.discovery import build
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Inicjalizacja API YouTube
youtube = build('youtube', 'v3', developerKey='API_KEY')

# Pobieranie playlist
playlists_request = youtube.playlists().list(
    part='snippet,contentDetails',
    channelId='CHANNEL_ID'
)

playlists_response = playlists_request.execute()

# Pobieranie filmów z playlisty
playlistitems_request = youtube.playlistItems().list(
    part='snippet,contentDetails',
    playlistId='PLAYLIST_ID',
    maxResults=50
)

playlistitems_response = playlistitems_request.execute()



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET',
    redirect_uri='http://localhost:8888/callback',
    scope='playlist-modify-private playlist-modify-public'
))

playlist = sp.user_playlist_create(user='USER_ID', name='Z YT')
playlist_id = playlist['id']

track_ids = []
for item in playlistitems_response['items']:
    # Zakładając, że `item['snippet']['title']` jest nazwą utworu
    print(item['snippet']['title'])
    track_name = item['snippet']['title']
    track_results = sp.search(q=track_name, type='track', limit=1)
    if track_results['tracks']['items']:
        # Dodajemy ID pierwszego znalezionego utworu do listy
        track_ids.append(track_results['tracks']['items'][0]['id'])

# Dodawanie utworów do playlisty na Spotify
if track_ids:
    sp.playlist_add_items(playlist_id=playlist_id, items=track_ids)
