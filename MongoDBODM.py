from pymongo import MongoClient

class MongoDBODM:
    def __init__(self, host='127.0.0.1', port=27017, username=None, password=None, auth_source='admin'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.auth_source = auth_source
        try:
            self.client = self.connect()
        except ConnectionError as e:
            print(f"Failed to connect to MongoDB: {e}")

    def connect(self):
        if self.username and self.password:
            uri = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.auth_source}"
        else:
            uri = f"mongodb://{self.host}:{self.port}/"
        return MongoClient(uri)

    def switch_database(self, database_name):
        self.current_database = self.client[database_name]

    def switch_collection(self, collection_name):
        self.current_collection = self.current_database[collection_name]

    def create_database(self, database_name):
        self.client[database_name]

    def delete_database(self, database_name):
        self.client.drop_database(database_name)

    def create_collection(self, collection_name):
        self.current_database.create_collection(collection_name)

    def delete_collection(self, collection_name):
        self.current_database.drop_collection(collection_name)

    def insert_one(self, document):
        return self.current_collection.insert_one(document)

    def insert_many(self, documents):
        return self.current_collection.insert_many(documents)

    def find_one(self, query=None):
        return self.current_collection.find_one(query)

    def find_many(self, query=None):
        return self.current_collection.find(query)

    def update_one(self, query, new_values):
        return self.current_collection.update_one(query, {'$set': new_values})

    def update_many(self, query, new_values):
        return self.current_collection.update_many(query, {'$set': new_values})

    def delete_one(self, query):
        return self.current_collection.delete_one(query)

    def delete_many(self, query):
        return self.current_collection.delete_many(query)

    def replace_one(self, query, replacement):
        return self.current_collection.replace_one(query, replacement)

    def replace_many(self, query, replacements):
        result = []
        for replacement in replacements:
            result.append(self.current_collection.replace_one(query, replacement))
        return result

    def rename_collection(self, old_name, new_name):
        self.current_database[old_name].rename(new_name)

    def rename_database(self, old_name, new_name):
        self.client.admin.command('copydb', fromdb=old_name, todb=new_name)
        self.client.drop_database(old_name)
