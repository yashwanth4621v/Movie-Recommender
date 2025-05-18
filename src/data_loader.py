import pandas as pd

def load_movielens_data(path):
    ratings = pd.read_csv(f"{path}/ratings.csv")
    movies = pd.read_csv(f"{path}/movies.csv")
    return ratings, movies
