from mongoengine import Document, StringField , IntField, FloatField
class Post(Document):
    n = StringField()
    i= StringField()
    e = StringField()
    p= IntField