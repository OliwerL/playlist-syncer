from googleapiclient.discovery import build
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Inicjalizacja API YouTube
youtube = build('youtube', 'v3', developerKey='AIP')

# Pobieranie playlist
playlists_request = youtube.playlists().list(
    part='snippet,contentDetails',
    channelId='UCeRQwPWr-2G2cfTTEYp7rLg'
)

playlists_response = playlists_request.execute()

# Pobieranie filmów z playlisty
playlistitems_request = youtube.playlistItems().list(
    part='snippet,contentDetails',
    playlistId='PLeBjddQ0xTRvDCyZ5oXLmYERvIm4s5dZa',
    maxResults=50
)

playlistitems_response = playlistitems_request.execute()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='TWÓJ_CLIENT_ID',
    client_secret='TWÓJ_CLIENT_SECRET',
    redirect_uri='http://localhost:8888/callback',
    scope='playlist-modify-private playlist-modify-public'
))

# Wyszukiwanie utworów
track_results = sp.search(q='nazwa utworu lub artysty', type='track')
track_ids = [track['id'] for track in track_results['tracks']['items']]

# Tworzenie playlisty
playlist = sp.user_playlist_create(user='User', name='Z YT')
playlist_id = playlist['id']

# Dodawanie utworów do playlisty
sp.playlist_add_items(playlist_id='playlist_id', items=track_ids)
