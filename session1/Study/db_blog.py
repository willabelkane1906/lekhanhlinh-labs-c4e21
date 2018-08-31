# 1. connect to database

from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://N.Dakota:ongbien36bahuong44@ds235352.mlab.com:35352/tandako"
client = MongoClient(uri)
db = client.get_default_database()


# 2. select collection
posts = db["posts"]

# 3. creat document
post = {
    "title": "tell me honestly",
    "content" : "would you still love me the same?"
}

# 4.insert document
# posts.insert_one(post)
# print("done")

post_list = posts.find()
# print(post_list[2])
# for post in post_list:  
    # post_list ~ collection ~list
    # print(post)
    # post ~ document ~ dictionary
cond = {
  "title": {
      "$regex": "If",
      "$options": "l",
  }
}
# regular expression
post = posts.find_one(cond)
print(post)




