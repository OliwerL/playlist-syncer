# YouTube to Spotify Playlist Transfer

This script automates the transfer of music from a YouTube playlist to a Spotify playlist by retrieving video titles from YouTube and searching for corresponding tracks on Spotify. If a match is found, the track is added to a new Spotify playlist.

## Prerequisites

- Python installed on your system.
- Developer accounts on both Google and Spotify platforms.
- API Key from Google Developer Console for YouTube API access.
- Client ID and Client Secret from Spotify Developer Dashboard.

## Setup

### Google Developer Console

1. Go to the Google Developer Console and create a project.
2. Enable the YouTube Data API v3 for your project.
3. In the credentials section, generate an API Key.

### Spotify Developer Dashboard

1. Visit the Spotify Developer Dashboard.
2. Create an application to obtain the Client ID and Client Secret.
3. Add `http://localhost:8888/callback` as the Redirect URI in the app settings.

## Configuration

To configure the script, you will need to replace the placeholder values in the code with your actual credentials:

- `API_KEY`: Your personal API Key from the Google Developer Console for the YouTube Data API.
- `CLIENT_ID` and `CLIENT_SECRET`: Your Spotify Client ID and Client Secret from the Spotify Developer Dashboard.
- `CHANNEL_ID`: The ID of the YouTube channel where your playlist is located.
- `PLAYLIST_ID`: The ID of the YouTube playlist you want to transfer songs from.
- `USER_ID`: Your Spotify user ID where the new playlist will be created.

These values ensure that the script has the necessary permissions to access YouTube content and create playlists on Spotify.

## Usage

After configuration, run the script to start the transfer process. The script will:

1. Fetch video titles from the specified YouTube playlist.
2. Search for each title on Spotify and gather the track IDs.
3. Create a new Spotify playlist named "Z YT".
4. Add the found tracks to the newly created Spotify playlist.
