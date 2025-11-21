import pandas as pd
import numpy as np

df = pd.read_csv('Data/imdb_top_1000.csv')

#addind the decade the movie was released
df['Decade'] = (df['Released_Year'] // 10) * 10

#mean of metactric and imdb rating to add "nuance"
df['Rating'] = np.where(
    df['Meta_score'].notna(),
    (df['IMDB_Rating'] * 10 + df['Meta_score']) / 2,
    df['IMDB_Rating'] * 10
)

# returning the top 10 directors with best average rating
def get_top_10_best_directors(df):
    return(df.groupby('Director')['Rating'].mean().nlargest(10))

# returning the top 10 most present directors
def get_top_10_directors(df):
    return(df['Director'].value_counts().nlargest(10))

# returning the director with best rating average for each decade
def get_best_director_per_decade(df):
    g = (
        df.groupby(['Decade', 'Director'])
          .agg(avg_rating=('Rating', 'mean'),
               movie_count=('Rating', 'size'))
          .reset_index()
    )

    # filter directors with >= 5 movies
    g = g[g['movie_count'] >= 2]

    return (
        g.sort_values(['Decade', 'avg_rating'], ascending=[True, False])
         .groupby('Decade')
         .head(1)
         .reset_index(drop=True)
    )

print(get_best_director_per_decade(df).head(25))