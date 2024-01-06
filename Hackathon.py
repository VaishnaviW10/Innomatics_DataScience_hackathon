import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\\Users\\VAISHNAVI\Desktop\\movie_data\\ratings.csv")
df1 = pd.read_csv(r"C:\\Users\\VAISHNAVI\\Desktop\\movie_data\\movies.csv")
df2 = pd.read_csv(r"C:\\Users\\VAISHNAVI\\Desktop\\movie_data\\tags.csv")
df3 = pd.read_csv(r"C:\\Users\\VAISHNAVI\\Desktop\\movie_data\\links.csv")
print(df)
print("Top 5 movies based on number ratings:")
groupby = df.groupby('movieId')['rating'].agg(['count', 'mean'])
merge = pd.merge(df1, groupby, on='movieId', how='inner')
filtered = merge[merge['count'] > 50]
topmovies = filtered.nlargest(5, 'count')
print(topmovies[['title', 'count']])
print("The movie Id of the highest IMDB rating:")
merge1 = pd.merge(df1, df, on='movieId', how='inner')
avg = merge1.groupby('movieId')['rating'].mean()
IMDB = avg.idxmax()
print(IMDB)
print("The movie Id of the Sci-Fi movie having highest IMDB rating:")
merged = pd.merge(df1, df, on='movieId', how='inner')
avg_rating = merged.groupby('movieId')['rating'].mean()

most_rated_scifi_movie_id = (
    merged[merged['genres'].str.contains('Sci-Fi')]
    .groupby('movieId')['rating']
    .mean()
    .idxmax()
)
print(most_rated_scifi_movie_id)