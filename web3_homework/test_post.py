import mlab
from post import Post

# 1. connect
mlab.connect()
# 2. create data
# p = Post(title="c4e21", author="quan", content="abc", likes=144)
# print(p.title)
# print(p.content)
# print(p.author)
# print(p.likes)
# # 3. write data
# p.save()

def test_load_data():
    # 2: test load all data
    all_posts = Post.objects()
    # lazyloading


 # 3. print all documents
    for post in all_posts:
        print(post.title)
        print(post.content)
        print(post.author)
        print("...........................")  

def test_load_one_data(post_id):
    print(post_id)
    post = Post.objects().with_id(post_id)
    if post is None:
        print("not found")
    else:
        print(post.title)
        print(post.author)
        print(post.content)
# test_load_one_data("")

def delete_one_data(post_id):
    # 1.retrive document
    post = Post.objects().with_id(post_id)
   

    # 2.delete document
    if post is None:
        print("Post not found")
    else:
        post.delete()

       
# delete_one_data("5ba0f8e51d2a750ea02c0fe6")

def update_one(post_id, new_title):
    # 1, retive post
    post = Post.objects().with_id(post_id)

    # 2.update
    # slug
    post.update(set__title=new_title)
update_one("5ba0f9721d2a751e20d3f0cc","corki")