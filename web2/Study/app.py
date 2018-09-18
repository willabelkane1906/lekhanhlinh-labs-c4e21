from flask import Flask, render_template, request
import mlab
from post import Post

app = Flask(__name__)
mlab.connect()
p = {
    "title" : "c4e21",
    "content" : "Module web, hackathon",
    "auther" : "Quan",
    "date" : "2018/09/02",
}
ps = [
    {
    "title" : "c4e21",
    "content" : "Module web, hackathon",
    "author" : "Quan",
    "date" : "2018/09/02",  
    },
    {
        "title" : "c4e21-hackathon",
    "content" : "abcd",
    "author" : "xys",
    "date" : "2018/09/02",
    },
    {
        "title" : "c4e21-fgtgtgfr",
    "content" : "rtgrtgt",
    "author" : "sungdja",
    "date" : "2018/09/02",
    }
]

@app.route("/post")
def post():
    return render_template("dict.html", post=p)

@app.route("/posts")
def posts():
    return render_template("dicts.html",posts=ps)


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template("new_post.html")
    elif request.method == "POST":
        # 1.get form and extract data
        form = request.form
        t = form["title"]
        a = form["author"]
        c = form["content"]
        
        

        # 2.add new post
        new_post = Post(title=t, author=a, content=c, likes=0)
        new_post.save()
        return "OK"
 


if __name__ == "__main__":
    app.run(debug=True)
