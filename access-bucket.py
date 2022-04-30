import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_account.json'

bucket_name = 'my-new-bucket'
storage_client = storage.Client(bucket_name)
bucket_location = 'us'

### Accesing an specific bucket

my_bucket = storage_client.get_bucket(bucket_name)