import pandas as pd
import numpy as np


def add_rating(df): #adds a new column rating that averages imdbs and metacritics ratings
    df['Rating'] = np.where(
    df['Meta_score'].notna(),
    (df['IMDB_Rating'] * 10 + df['Meta_score']) / 2,
    df['IMDB_Rating'] * 10
    )

def add_decade(df): #adding a decade column
    df['Decade'] = (df['Released_Year'] // 10) * 10

def explode_genre(df): #creating a new Data frame exploding the genre column to agregate easier on genre querries 
    df_exploded = df
    df_exploded['Genre'] = df['Genre'].fillna('').astype(str).str.split(r',\s*')
    df_exploded = df.explode('Genre')
    return(df_exploded)

def melt_actors(df): #creating a new data frame focusing on actors to agregate easier
    return(df.melt(id_vars=['Series_Title', 'Gross'],value_vars=("Star1","Star2","Star3","Star4"), var_name='Role',value_name='Actor'))