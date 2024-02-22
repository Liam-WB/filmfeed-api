import os
import requests

if os.path.exists('env.py'):
    import env

OMDB_API_KEY = os.environ.get('OMDB_API_KEY')

def test_api(title):
    print('Key works')
    url = f'https://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)


test_api('Iron')

