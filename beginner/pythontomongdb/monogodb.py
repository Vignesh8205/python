from pymongo import MongoClient

# Create a connection
client = MongoClient('mongodb://localhost:27017')

# Access a database
db = client['vicky']

# Access a collection
collection = db['vi']

# Insert a document
# document = {'_id':'24','name': 'guna','lastname':'r','age':'21'}
# insert= collection.insert_one(document)
# if insert:
#     print('inserted')
# else:
#     print('not inserted')


# view document
    
view=collection.find()

for i in view:
    print(i)

# view one
document_id=input('enter yuor id:')
view_one=collection.find_one({'_id': document_id})
print(view_one)
# delete all
delete_all=collection.delete_many({"python":"connesct"})
if delete_all:
    print('delted succes')

# delete one
document_id1=input('enter your delete id:')
delete_one=collection.delete_one({'_id':document_id1})

# update document
update_id=input('enter your update id:')
update_data = {
    '$set': {'age': '23'}
}
# update 
collection.update_one({'_id':update_id},update_data)
# Close the connection
client.close()
