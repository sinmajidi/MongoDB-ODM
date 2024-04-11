# MongoDB Object-Document Mapper (ODM)

This Python class provides an Object-Document Mapper (ODM) for MongoDB, simplifying interactions with MongoDB databases and collections by abstracting away the low-level details of the PyMongo library.

## Installation

Ensure you have `pymongo` installed. You can install it via pip:

```bash
pip install pymongo
```

## Usage

1. Import the `MongoDBODM` class from `MongoDBODM.py`:

```python
from MongoDBODM import MongoDBODM
```
2. Create an instance of MongoDBODM with optional parameters for host, port, username, password, and authentication source:
```python
mongo_odm = MongoDBODM(host='127.0.0.1', port=27017, username='your_username', password='your_password')
```
If authentication is not required, you can omit the username and password parameters:
```python
mongo_odm = MongoDBODM(host='127.0.0.1', port=27017)
```

3. Switch to a specific database:
```python
mongo_odm.switch_database('my_database')

```
4. Create a new database (optional):
```python
mongo_odm.create_database('another_database')
```
5. Switch to a specific collection:
```python
mongo_odm.switch_collection('my_collection')
```
6. Create a new collection (optional):
```python
mongo_odm.create_collection('another_collection')
```
7. Perform CRUD operations:
```python
# Insert a single document
insert_one_result = mongo_odm.insert_one({"name": "Alice", "age": 25})

# Insert multiple documents
insert_many_result = mongo_odm.insert_many([{"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}])

# Find a single document
found_document = mongo_odm.find_one({"name": "Alice"})

# Find multiple documents
found_documents = mongo_odm.find_many({"age": {"$gt": 25}})

# Update a document
update_result = mongo_odm.update_one({"name": "Alice"}, {"age": 26})

# Update many documents
update_result = mongo_odm.update_many({"age": {"$lt": 30}}, {"status": "Young"})

# Delete a document
delete_result = mongo_odm.delete_one({"name": "Bob"})

# Delete multiple documents
delete_many_result = mongo_odm.delete_many({"age": {"$gt": 30}})

# Replace a document
replace_result = mongo_odm.replace_one({"name": "Charlie"}, {"name": "David", "age": 40})

# Replace many documents
replace_many_result = mongo_odm.replace_many({"age": {"$gt": 30}}, [{"name": "Dave", "age": 40}, {"name": "Eve", "age": 45}])

# Rename a collection
mongo_odm.rename_collection('my_collection', 'renamed_collection')

# Rename a database
mongo_odm.rename_database('my_database', 'renamed_database')

# Delete a collection
mongo_odm.delete_collection('another_collection')

# Delete a database
mongo_odm.delete_database('another_database')

```

8. Close the connection to MongoDB when done:
```python
mongo_odm.client.close()

```

## Class Methods
* `switch_database(database_name)`: Switch to the specified database.
* `switch_collection(collection_name)`: Switch to the specified collection.
* `create_database(database_name)`: Create a new database.
* `delete_database(database_name)`: Delete a database.
* `create_collection(collection_name)`: Create a new collection.
* `delete_collection(collection_name)`: Delete a collection.
* `insert_one(document)`: Insert a single document.
* `insert_many(documents)`: Insert multiple documents.
* `find_one(query=None)`: Find a single document matching the query.
* `find_many(query=None)`: Find multiple documents matching the query.
* `update_one(query, new_values)`: Update a single document matching the query.
* `update_many(query, new_values)`: Update multiple documents matching the query.
* `delete_one(query)`: Delete a single document matching the query.
* `delete_many(query)`: Delete multiple documents matching the query.
* `replace_one(query, replacement)`: Replace a single document matching the query.
* `replace_many(query, replacements)`: Replace multiple documents matching the query.
* `rename_collection(old_name, new_name)`: Rename a collection.
* `rename_database(old_name, new_name)`: Rename a database.
## Afra IOT

This MongoDB Object-Document Mapper (ODM) is developed for [Afra IOT](https://afraiot.org/), a startup dedicated to providing innovative Internet of Things (IoT) solutions. Afra IOT focuses on leveraging technology to improve efficiency, productivity, and sustainability across various industries.

For more information about Afra IOT and its projects, visit [AfraIOT.org](https://afraiot.org/).