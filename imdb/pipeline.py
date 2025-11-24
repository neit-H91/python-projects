import pandas as pd
from Scripts import extract, transform, log
import logging


# Setup logging
log.setup_logging()

def main():
    # Load raw data
    df = extract.load_csv('Data/raw/imdb_top_1000.csv')

    # Clean gross and runtime
    extract.clean_gross(df)
    extract.clean_runtime(df)

    # Define expected schema and types (example, adjust as needed)
    expected_schema = ['Poster_Link', 'Series_Title', 'Released_Year', 'Certificate', 'Runtime',
                       'Genre', 'IMDB_Rating', 'Overview', 'Meta_score', 'Director', 'Star1',
                       'Star2', 'Star3', 'Star4', 'No_of_Votes', 'Gross', 'Number_of_Movies']
    expected_types = {
        'Poster_Link': 'object',
        'Series_Title': 'object',
        'Released_Year': 'int64',
        'Certificate': 'object',
        'Runtime': 'int64',
        'Genre': 'object',
        'IMDB_Rating': 'float64',
        'Overview': 'object',
        'Meta_score': 'float64',
        'Director': 'object',
        'Star1': 'object',
        'Star2': 'object',
        'Star3': 'object',
        'Star4': 'object',
        'No_of_Votes': 'int64',
        'Gross': 'float64',
        'Number_of_Movies' : 'int64'
    }

    # Validate schema
    schema_ok = extract.check_schema(expected_schema, df)
    log.log_schema_result(schema_ok)

    # Validate dtypes
    dtype_result = extract.validate_dtypes(df, expected_types)
    log.log_dtype_validation(dtype_result)

    # Check dates
    date_result = extract.date_check(df, 1895, 'Released_Year')
    log.log_date_check(date_result)

    # Check IMDB rating
    rating_result = extract.imdb_rating_check(df)
    log.log_imdb_rating_check(rating_result)

    # Check meta score
    score_result = extract.meta_score_check(df)
    log.log_meta_score_check(score_result)

    # Check uniqueness (assume by Series_Title and Released_Year)
    unique_cols = ['Series_Title', 'Released_Year']
    unique_result = extract.unique_check(df, unique_cols)
    log.log_unique_check(unique_result, unique_cols)

    # Check runtime positive
    runtime_result = extract.runtime_check(df, 'Runtime')
    log.log_runtime_check(runtime_result, 'Runtime')

    # Check gross non-negative
    gross_result = extract.gross_check(df, 'Gross')
    log.log_gross_check(gross_result, 'Gross')

    # Check nulls
    nulls = extract.check_nulls(df)
    log.log_null_check(nulls)

    # Now transform
    transform.add_decade(df)
    transform.add_rating(df)

    # Save cleaned data
    import os
    if not os.path.exists('Data/cleaned'):
        os.makedirs('Data/cleaned')
    df.to_csv('Data/cleaned/cleaned_imdb.csv', index=False)

    # Additional transforms for analysis
    df_exploded = transform.explode_genre(df.copy())
    df_actors = transform.melt_actors(df.copy())

    df_exploded.to_csv('Data/cleaned/cleaned_imdb_genres.csv', index=False)
    df_actors.to_csv('Data/cleaned/cleaned_imdb_actors.csv', index=False)

    # Log completion
    logger = logging.getLogger('imdb_logger')
    logger.info("Pipeline completed successfully. Cleaned data saved.")

if __name__ == "__main__":
    main()
