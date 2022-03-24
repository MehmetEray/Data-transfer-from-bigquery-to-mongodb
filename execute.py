def execute(self, context):
    blobs = self.get_blobs()
    self.insert_into_mongo(blobs)