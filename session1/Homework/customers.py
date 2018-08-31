from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()
customers = db["customers"]


from collections import Counter 
cond1 = {  'ref' : 'events'}
count1 = customers.find(cond1).count()
print("events:",count1)

cond2 = {  'ref' : 'ads'}
count2 = customers.find(cond2).count()
print("advertisements:",count2)

cond3 = {  'ref':'wom'}
count3 = customers.find(cond3).count()
print("word of mouth:",count3)


from matplotlib import pyplot
counts = [count1, count2, count3]
names = ["events","advertisements","word of mouth"]
pyplot.pie(counts, labels=names, autopct="%.1f%%", shadow=True, explode=[0,0.1,0])
pyplot.title("marketing database")
pyplot.axis("equal")
pyplot.show()





