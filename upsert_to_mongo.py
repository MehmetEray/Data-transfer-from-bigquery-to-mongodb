if self.filter_field is None:
    try:
        # insert data
        hook.insert_many(self.collection_name, docs=message,
                         mongo_db=self.db_name)
    except Exception as err:
        print("ERROR : " + str(err))
else:
    try:
        # replace data with current data
        hook.replace_many(mongo_collection=self.collection_name,
                          docs=message, filter_docs=[
                {self.filter_field: doc[self.filter_field]} for doc in message],
                          mongo_db=self.db_name,
                          upsert=self.upsert)

    except Exception as err:
        print("ERROR : " + str(err))