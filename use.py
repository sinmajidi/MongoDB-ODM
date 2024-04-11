from MongoDBODM import MongoDBODM  # Import the MongoDBODM class

# Create an instance of MongoDBODM
mongo_odm = MongoDBODM(host='127.0.0.1', port=27017)

# Switch to a specific database
mongo_odm.switch_database('my_database')

# Create a new database
mongo_odm.create_database('another_database')

# Switch to a specific collection
mongo_odm.switch_collection('my_collection')

# Create a new collection
mongo_odm.create_collection('another_collection')

# Define documents for insertion
document1 = {"name": "Alice", "age": 25}
document2 = {"name": "Bob", "age": 30}
document3 = {"name": "Charlie", "age": 35}
documents = [document1, document2, document3]

# Insert a single document
insert_one_result = mongo_odm.insert_one(document1)
print("Insert One Result:", insert_one_result)

# Insert multiple documents
insert_many_result = mongo_odm.insert_many(documents)
print("Insert Many Result:", insert_many_result)

# Find a single document
find_one_query = {"name": "Alice"}
found_document = mongo_odm.find_one(find_one_query)
print("Find One Result:", found_document)

# Find multiple documents
find_many_query = {"age": {"$gt": 25}}  # Find documents where age is greater than 25
found_documents = mongo_odm.find_many(find_many_query)
print("Find Many Result:")
for document in found_documents:
    print(document)

# Update a document
update_query = {"name": "Alice"}
new_values = {"age": 26}
update_result = mongo_odm.update_one(update_query, new_values)
print("Update Result:", update_result)


# Update many document
update_query = {"age": {"$lt": 30}}  # Update documents where age is less than 30
new_values = {"status": "Young"}
update_result = mongo_odm.update_many(update_query, new_values)
print("Update Many Result:", update_result)


# Delete a document
delete_query = {"name": "Bob"}
delete_result = mongo_odm.delete_one(delete_query)
print("Delete Result:", delete_result)

# Delete multiple documents
delete_many_query = {"age": {"$gt": 30}}  # Delete documents where age is greater than 30
delete_many_result = mongo_odm.delete_many(delete_many_query)
print("Delete Many Result:", delete_many_result)

# Replace a document
replace_query = {"name": "Charlie"}
replacement = {"name": "David", "age": 40}
replace_result = mongo_odm.replace_one(replace_query, replacement)
print("Replace Result:", replace_result)


# Define replacements for replace_many
replacement1 = {"name": "Dave", "age": 40}
replacement2 = {"name": "Eve", "age": 45}
replacements = [replacement1, replacement2]

# Replace multiple documents
replace_query = {"age": {"$gt": 30}}  # Replace documents where age is greater than 30
replace_many_result = mongo_odm.replace_many(replace_query, replacements)
print("Replace Many Result:", replace_many_result)


# Rename a collection
mongo_odm.rename_collection('my_collection', 'renamed_collection')

# Rename a database
mongo_odm.rename_database('my_database', 'renamed_database')

# Delete a collection
mongo_odm.delete_collection('another_collection')

# Delete a database
mongo_odm.delete_database('another_database')

# Close the connection to MongoDB
mongo_odm.client.close()
