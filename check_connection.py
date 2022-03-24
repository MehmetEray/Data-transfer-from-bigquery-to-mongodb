if check_connection:
    for blob in blobs:
        blob_full_path = f'gs://{self.source_bucket_name}/{blob.name}'
        if blob.name.endswith('.json'):
            print('will insert full_path:  ' + blob_full_path)
            message = json.loads(blob.download_as_string())