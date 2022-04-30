import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_account.json'

## List bucket details

bucket_name = 'my-new-bucket'
storage_client = storage.Client(bucket_name)
bucket_location = 'us'

vars(bucket_name)