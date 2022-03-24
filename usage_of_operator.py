gcs_json_to_mongo = GcsJsonToMongoDb(
    task_id='gcs_json_to_mongo',
    source_bucket_name=json.loads(Variable.get('example'))['bucket_name'],
    source_bucket_prefix=json.loads(Variable.get('example'))['source_prefix'],
    mongo_conn_id=json.loads(Variable.get('example'))['mongo_conn_id'],
    collection_name=json.loads(Variable.get('example'))['mongo_collection_name'],
    upsert=True
)