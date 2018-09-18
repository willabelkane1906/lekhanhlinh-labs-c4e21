import mlab
from post import Post

# 1. connect
mlab.connect()
# 2. create data
p = Post(title="c4e21", author="quan", content="abc", likes=144)
print(p.title)
print(p.content)
print(p.author)
print(p.likes)
# 3. write data
p.save()