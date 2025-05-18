import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def content_based_recommendations(movies_df, user_ratings):
    tfidf = TfidfVectorizer(stop_words='english')
    movies_df['genres'] = movies_df['genres'].fillna('')
    tfidf_matrix = tfidf.fit_transform(movies_df['genres'])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    movie_indices = pd.Series(movies_df.index, index=movies_df['movieId'])

    watched_indices = [movie_indices[movieId] for movieId in user_ratings['movieId']]
    scores = cosine_sim[watched_indices].mean(axis=0)

    movie_scores = list(enumerate(scores))
    movie_scores = sorted(movie_scores, key=lambda x: x[1], reverse=True)

    top_movies = [movies_df.iloc[i[0]] for i in movie_scores if movies_df.iloc[i[0]]['movieId'] not in user_ratings['movieId']]
    return pd.DataFrame(top_movies[:10])
