import pandas as pd
import numpy as np

df = pd.read_csv('Data/imdb_top_1000.csv')

df['Rating'] = np.where(
    df['Meta_score'].notna(),
    (df['IMDB_Rating'] * 10 + df['Meta_score']) / 2,
    df['IMDB_Rating'] * 10
)

df_exploded = df

df_exploded['Genre'] = df['Genre'].fillna('').astype(str).str.split(r',\s*')

df_exploded = df.explode('Genre')

def get_top_10_best_films(df):
    return(df.sort_values(by='Rating',ascending=False).head(10))

def get_top_10_gross(df):
    return(df.sort_values(by='Gross',ascending=False).head(10))

def get_top_10_most_voted(df):
    return(df.sort_values(by='No_of_Votes',ascending=False).head(10))

def get_rating_distribution(df):
    return(df['Rating'].value_counts().sort_index())

def get_genre_distribution(df):
    return(df['Genre'].value_counts().sort_index())

def get_top_10_best_directors(df):
    return(df.groupby('Director')['Rating'].mean().nlargest(10))

def get_top_10_directors(df):
    return(df['Director'].value_counts().nlargest(10))

def get_top_movies_per_genre(df): 
    return(df.groupby('Genre').apply(lambda x: x.nlargest(10, 'Rating')['Series_Title']))

def get_top_movies_per_director(df):
    return(df.groupby('Director').apply(lambda x: x.nlargest(5, 'Rating')['Series_Title']))

def get_top_years(df):
    df_filtered = df[df.groupby('Released_Year')['Rating'].transform('size') > 10]
    top_years = df_filtered.groupby('Released_Year')['Rating'].mean().nlargest(10)
    return(top_years)

def get_top_gross_years(df):
    df['Gross'] = df['Gross'].str.replace(',', '').astype(float)
    return(df.groupby('Released_Year')['Gross'].sum().sort_values(ascending=False).head(10))

df_actors = df.melt(id_vars=['Series_Title', 'Gross'],value_vars=("Star1","Star2","Star3","Star4"), var_name='Role',value_name='Actor')

df_actors['Gross'] = df['Gross'].str.replace(',', '').astype(float)
# print(df_actors.groupby('Actor').mean('Gross').sort_values('Gross',ascending=False))

df['Gross'] = df['Gross'].str.replace(',', '').astype(float)
print(df.groupby('Director')['Gross'].mean().sort_values(ascending=False))