from django.http import JsonResponse
from django.shortcuts import render
# from .spotify_utils import fetch_spotify_genres
import requests

SPOTIFY_TOKEN = '816852b3a16b43babd50e5659d1b4645'

def fetch_categories():
    url = 'https://api.spotify.com/v1/browse/categories'
    headers = {'Authorization': f'Bearer {SPOTIFY_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

def fetch_tracks(category_id):
    url = f'https://api.spotify.com/v1/browse/categories/{category_id}/playlists'
    headers = {'Authorization': f'Bearer {SPOTIFY_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

def categories_view(request):
    categories = fetch_categories()
    return render(request, 'musicapp/categories.html', {'categories': categories})

def tracks_view(request, category_id):
    tracks = fetch_tracks(category_id)


    
# def get_spotify_genres(request):
#     access_token = '1POdFZRZbvb...qqillRxMr2z'  # Replace with your token
#     genres = fetch_spotify_genres(access_token)
#     return JsonResponse(genres)

# def get_track(request, track_id):
#     # Set the URL and the authorization token
#     url = f'https://api.spotify.com/v1/tracks/{track_id}'
#     headers = {
#         'Authorization': 'Bearer NgCXRK...MzYjw'
#     }

#     # Make the GET request
#     response = requests.get(url, headers=headers)

#     # Check if the request was successful
#     if response.status_code == 200:
#         track_data = response.json()  # Parse the JSON response
#         return JsonResponse(track_data)  # Return the data as JSON
#     else:
#         return JsonResponse({'error': response.text}, status=response.status_code)
    return render(request, 'musicapp/tracks.html', {'tracks': tracks})