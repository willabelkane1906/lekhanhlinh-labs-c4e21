from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()

posts = db["posts"]
post = {
    "title": "the sound of silence",
    "content" : '''
    Within the sound of silence
    In restless dreams I walked alone
    Narrow streets of cobblestone
   'Neath the halo of a street lamp
    I turned my collar to the cold and damp
    When my eyes were stabbed by the flash of a neon light
    That split the night
    And touched the sound of silence''',
    "author" : "Disturbed",
    }


posts.insert_one(post)
print("done")


