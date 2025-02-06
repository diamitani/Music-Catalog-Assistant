import requests
from dotenv import load_dotenv
import os

load_dotenv()

SPOTIFY_API_URL = "https://api.spotify.com/v1/search"
SPOTIFY_ACCESS_TOKEN = os.getenv('SPOTIFY_ACCESS_TOKEN')

def fetch_spotify_metadata(track_name, artist_name):
    headers = {"Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"}
    params = {
        'q': f'track:{track_name} artist:{artist_name}',
        'type': 'track',
        'limit': 1
    }
    response = requests.get(SPOTIFY_API_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        tracks = response.json().get('tracks', {}).get('items', [])
        if tracks:
            track = tracks[0]
            return {
                'title': track['name'],
                'album': track['album']['name'],
                'artist': track['artists'][0]['name'],
                'release_date': track['album']['release_date'],
                'isrc': track['external_ids'].get('isrc')
            }
    return {}

def validate_and_enrich(metadata):
    if 'isrc' not in metadata or not metadata['isrc']:
        enriched_data = fetch_spotify_metadata(metadata.get('title', ''), metadata.get('artist', ''))
        metadata.update(enriched_data)
    return metadata
