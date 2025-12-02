from google.cloud import storage, bigquery

storage_client = storage.Client() 

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

def create_bigquery_dataset(dataset_id):
    """Creates a BigQuery dataset if it does not already exist."""
    bigquery_client = bigquery.Client()

    # Construct a full Dataset object to send to the API.
    # The client library will use your default project.
    dataset_ref = bigquery_client.dataset(dataset_id)
    dataset = bigquery.Dataset(dataset_ref)

    # Specify the geographic location where the dataset should reside.
    dataset.location = "US"

    # Send the dataset to the API for creation.
    # The `exists_ok=True` parameter prevents an error if the dataset already exists.
    dataset = bigquery_client.create_dataset(dataset, exists_ok=True)
    print(f"Dataset {dataset.dataset_id} created or already exists.")

def load_csv_to_bigquery(bucket_name, file_name, dataset_id, table_id):
    """Loads a CSV file from GCS into a BigQuery table."""
    bigquery_client = bigquery.Client()

    # Set table_id to the full destination table ID.
    table_ref = bigquery_client.dataset(dataset_id).table(table_id)

    # Configure the load job
    job_config = bigquery.LoadJobConfig(
        # Let BigQuery automatically detect the schema.
        autodetect=True,
        # Specify the source format.
        source_format=bigquery.SourceFormat.CSV,
        # Skip the header row.
        skip_leading_rows=1,
    )

    uri = f"gs://{bucket_name}/{file_name}"

    load_job = bigquery_client.load_table_from_uri(
        uri, table_ref, job_config=job_config
    )  # Make an API request.

    print(f"Starting job {load_job.job_id} to load {uri} into {dataset_id}.{table_id}")
    load_job.result()  # Waits for the job to complete.
    print(f"Job finished. Loaded {load_job.output_rows} rows.")