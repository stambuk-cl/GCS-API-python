from logging import exception
import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_account.json'

bucket_name = 'my-new-bucket'
storage_client = storage.Client(bucket_name)
bucket_location = 'us'

### Upload files

def upload_to_bucket(bucket_name, file_path, destination_blob_name):
	try:
		bucket = storage_client.get_bucket(bucket_name)
		blob = bucket.blob(destination_blob_name)
		blob.upload_from_filename(file_path)
	except Exception as e:
		print(e)
file_path = './test.txt'
upload_to_bucket(bucket_name, file_path, 'test.txt')