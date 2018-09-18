import mongoengine

host = "ds257752.mlab.com"
port = 57752
db_name = "c4e21_blog"
user_name = "admin"
password = "abc1234"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())