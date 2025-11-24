import pandas as pd
import numpy as np
import logging
import os
from datetime import datetime

def setup_logging():
    # Get logs directory relative to Scripts/
    logs_dir = os.path.join(os.path.dirname(__file__), '..', 'Logs')
    # Create logs directory if not exists
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    # Get current date in dd_mm_yyyy format
    current_date = datetime.now().strftime('%d_%m_%Y')
    log_filename = os.path.join(logs_dir, f'pipeline_{current_date}.log')
    # Configure logger
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def get_logger():
    return logging.getLogger('imdb_logger')

def log_schema_result(result):
    logger = logging.getLogger('imdb_logger')
    logger.info('Schema check started.')
    if result:
        logger.info('Schema check passed: Columns match expected schema.')
    else:
        logger.error('Schema check failed: Columns do not match expected schema.')

def log_dtype_validation(result_df):
    logger = logging.getLogger('imdb_logger')
    logger.info('Data type validation started.')
    for _, row in result_df.iterrows():
        if row['match']:
            logger.info(f"Column '{row['column']}' type check passed: Expected and actual type is '{row['expected']}'.")
        else:
            logger.error(f"Column '{row['column']}' type check failed: Expected '{row['expected']}', but got '{row['actual']}'.")

def log_date_check(result):
    logger = logging.getLogger('imdb_logger')
    logger.info('Date check started.')
    if result is True:
        logger.info('Date check passed: All dates are within the valid range.')
    else:
        logger.error(f'Date check failed: Invalid rows found:\n{result}')

def log_imdb_rating_check(result):
    logger = logging.getLogger('imdb_logger')
    logger.info('IMDB rating check started.')
    if result is True:
        logger.info('IMDB rating check passed: All ratings are within 0-10.')
    else:
        logger.error(f'IMDB rating check failed: Invalid rows found:\n{result}')

def log_meta_score_check(result):
    logger = logging.getLogger('imdb_logger')
    logger.info('Meta score check started.')
    if result is True:
        logger.info('Meta score check passed: All scores are within 0-100.')
    else:
        logger.error(f'Meta score check failed: Invalid rows found:\n{result}')

def log_unique_check(result, cols):
    logger = logging.getLogger('imdb_logger')
    logger.info('Uniqueness check started.')
    if result is True:
        logger.info(f'Uniqueness check passed: Combination of columns {cols} is unique.')
    else:
        logger.error(f'Uniqueness check failed: Duplicate rows found:\n{result}')

def log_runtime_check(result, col):
    logger = logging.getLogger('imdb_logger')
    logger.info('Runtime check started.')
    if result is True:
        logger.info(f'Runtime check passed: All values in column {col} are positive.')
    else:
        logger.error(f'Runtime check failed: Invalid rows found:\n{result}')

def log_gross_check(result, col):
    logger = logging.getLogger('imdb_logger')
    logger.info('Gross check started.')
    if result is True:
        logger.info(f'Gross check passed: All values in column {col} are non-negative.')
    else:
        logger.error(f'Gross check failed: Invalid rows found:\n{result}')

def log_null_check(nulls):
    logger = logging.getLogger('imdb_logger')
    logger.info('Null check started.')
    logger.info(f'Null counts: \n{nulls}')
