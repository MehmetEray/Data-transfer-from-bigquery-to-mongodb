def get_blobs(self):
    client = storage.Client()
    blobs = client.list_blobs(self.source_bucket_name,     prefix=self.source_bucket_prefix)
    return blobs