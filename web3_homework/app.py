from flask import Flask, render_template, request, redirect, url_for
import mlab
from post import Post

app = Flask(__name__)
mlab.connect()



@app.route("/post/<post_id>")
def post(post_id):
    post = Post.objects().with_id(post_id)
    return render_template("post_retail.html", post=post)

@app.route("/posts")
def posts():
    all_posts = Post.objects()
    return render_template("posts.html",posts=all_posts)

@app.route("/delete/<post_id>")
def delete_post(post_id):
    post = Post.objects().with_id(post_id)
    post.delete()
    return redirect(url_for("posts"))


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template("new_post.html")
    elif request.method == "POST":
        # 1.get form and extract data
        form = request.form
        title = form["title"]
        author = form["author"]
        content = form["content"]
        
        

        # 2.add new post
        new_post = Post(title=title, author=author, content=content, likes=0)
        new_post.save()
        return redirect(url_for("posts"))
 
@app.route("/update/<post_id>")
def update(post_id):
    p = Post.objects().with_id(post_id)
    if request.method == "GET":
        return render_template("update_post.html", post = p)
    elif request.method == "POST":
        form = request.form
        title = form["title"]
        author = form["author"]
        content = form["content"]
        post.update(set__title = title, set__author = author, set__content = content)
        return redirect(url_for("posts"))
    



if __name__ == "__main__":
    app.run(debug=True)
