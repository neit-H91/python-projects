import pandas as pd

df = pd.read_csv('Data/imdb_top_movies.csv')

df_exploded = df

df_exploded['Genres'] = df['Genres'].fillna('').astype(str).str.split(r',\s*')

df_exploded = df.explode('Genres')

def get_top_n_genres(df,n):
    return(df.groupby('Genres')['Genres'].count().nlargest(n))

def get_top_n_year(df,n):
    return(df.groupby(['Released_Year'])['Released_Year'].count().nlargest(n))

def get_top_n_director(df,n):
    return(df.groupby(['Director'])['Director'].count().nlargest(n))

def get_top_n_best_genres(df,n):
    return(df.groupby('Genres')['Rating'].mean().nlargest(n))

# print(get_top_n_genres(df_exploded,15))
# print(get_top_n_director(df,5))
# print(df.groupby('Director')['IMDB_Rating'].mean().nlargest(25))

# print(df.groupby('Released_Year').filter(lambda g: len(g) > 10).groupby('Released_Year')['IMDB_Rating'].mean().nlargest(10))

# print(df.loc[df['Director']=='Frank Darabont']['IMDB_Rating'])

# pd.set_option('display.max_rows',None)

# print(df.groupby('Released_Year')['Released_Year'].count())

print(get_top_n_best_genres(df_exploded,10))