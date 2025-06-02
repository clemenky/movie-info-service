import requests
import os
from config import TMDB_ACCESS_TOKEN


ACCESS_TOKEN = os.environ.get('TMDB_ACCESS_TOKEN')
BASE_URL = 'https://api.themoviedb.org/3'
HEADERS = {
    'accept': 'application/json',
    'Authorization': f'Bearer {TMDB_ACCESS_TOKEN}'
}

def request(endpoint, params=None):
    url = f'{BASE_URL}/{endpoint}'
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f'[TMDB API Error] {e}')
        return None

def search_by_title(movie_title, page):
    return request('search/movie', params={'query': movie_title, 'page': page})

def get_movie_details(movie_id):
    return request(f'movie/{movie_id}', params={'append_to_response': 'credits,release_dates'})

API_ENDPOINTS = {
    'search_by_title': {
        'function': search_by_title,
        'required_params': ['title', 'page']
    },
    'get_movie_details': {
        'function': get_movie_details,
        'required_params': ['movie_id']
    }
}

__all__ = [API_ENDPOINTS]