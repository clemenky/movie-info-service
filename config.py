from dotenv import load_dotenv
import os


load_dotenv()

MOVIE_SEARCH_PORT = os.getenv('MOVIE_SEARCH_PORT')
TMDB_ACCESS_TOKEN = os.getenv('TMDB_ACCESS_TOKEN')
