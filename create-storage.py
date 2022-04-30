import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_account.json'

## Create a new bucket
bucket_name = 'my-new-bucket'
storage_client = storage.Client(bucket_name)
bucket_location = 'us'
bucket = storage_client.create_bucket(bucket_name)