import pandas as pd
import numpy as numpy
from datetime import datetime

def date_check(df,min_year,col):
    max_year = datetime.now().year
    invalid_rows = df[~df[col].between(min_year, max_year)]
    if invalid_rows.empty:
        return True
    else:
        return invalid_rows
    
def imdb_rating_check(df):
    invalid_rows = df[~df['imdb_rating'].between(0, 10)]
    if invalid_rows.empty:
        return True
    else:
        return invalid_rows
    
def meta_score_check(df):
    invalid_rows = df[~df['meta_score'].between(0, 100)]
    if invalid_rows.empty:
        return True
    else:
        return invalid_rows