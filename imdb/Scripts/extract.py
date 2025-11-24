import pandas as pd
import numpy as np
from datetime import datetime

#loading raw files and checking data

def load_csv(file):
    return(pd.read_csv(file))

def check_schema(schema,df): #checks that columns have the expected name and no missing or unexpected col
    return(schema == list(df))

def validate_dtypes(df,expected_types): #checking each column and comparing its type to the expected one, returns a check dataframe
    result = []
    for col in df.columns:
        expected = expected_types.get(col, None)
        actual = str(df[col].dtype)
        result.append({
            "column": col,
            "expected": expected,
            "actual": actual,
            "match": actual == expected
        })
    return(pd.DataFrame(result))

def date_check(df,min_year,col): #checks that released year are within a valid range
    max_year = datetime.now().year
    invalid_rows = df[~df[col].between(min_year, max_year)]
    if invalid_rows.empty:
        return True
    else:
        return invalid_rows
    
def imdb_rating_check(df): #checks that imdb ratings are within 0-10
    invalid_rows = df[~df['IMDB_Rating'].between(0, 10)]
    if invalid_rows.empty:
        return True
    else:
        return invalid_rows
    
def meta_score_check(df): #checks that metacritics scores are within 0-100 (ignoring NaN as valid)
    invalid_rows = df[df['meta_score'].notna() & (~df['meta_score'].between(0, 100))]
    if invalid_rows.empty:
        return True
    else:
        return invalid_rows
    
def unique_check(df,cols): #checks that the combination of columns is unique
    duplicated = df[df.duplicated(subset=cols, keep=False)]
    if duplicated.empty:
        return True
    else:
        return duplicated
    
def runtime_check(df,col): #checks that runtimes are positive
    invalid_rows = df[df[col] <= 0]
    if invalid_rows.empty:
        return True
    else:
        return invalid_rows
    
def gross_check(df,col): #checks that gross values are positive
    invalid_rows = df[df[col] < 0]
    if invalid_rows.empty:
        return True
    else:
        return invalid_rows

def clean_gross(df): #changing gross from str with , to a float
    df['Gross'] = df['Gross'].str.replace(',', '').astype(float)

def clean_runtime(df): #changing runtime from str with ' min' to an int
    df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(int)

def check_nulls(df): #checking for nulls in dataframe
    return(df.isnull().sum())
