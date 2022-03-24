hook = MongoHook(conn_id=self.mongo_conn_id)
check_connection = hook.get_conn()