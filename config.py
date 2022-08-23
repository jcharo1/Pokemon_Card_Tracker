import os

SECRET_KEY = os.urandom(32)
password = os.getenv('PASS')
# database_path= f'postgresql://postgres:{password}@charo.gg/poketrack'
database_path= f'postgresql://localhost:5432/poketrack'
