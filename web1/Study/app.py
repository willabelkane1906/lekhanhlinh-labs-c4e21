# 1.create a flask app
from flask import Flask, render_template

app = Flask(__name__)
# 2.create router
ps = [
        "far far a way",
        "the art of happiness"    
    ]
@app.route("/posts/<int:position>")

def page(pos):
    post = ps[position -1 ]

    return render_template("post_detail.html",post=post )

@app.route("/")
def homepage():
    return render_template("homepage.html", posts=ps, fast="once upon the time")



@app.route("/linh")
def abcpage():
    return "hll"

@app.route("/blabla")
def dotdotpage():
    return "gabriel"

@app.route("/hello/<name>")
def hello(name):
    return "hello, " + name

@app.route("/add/<i>/<j>")
def tong(i , j):
    result = int(i) + int(j)
    print(result)
    return str(result)

@app.route("/addd/<int:i>/<int:j>")
def add(i,j):
    return str(i + j)

@app.route("/h1tag")
def h1tag():
    return "<h1>Heading 1 - Biggg</h1><p>inner peace</p>"

# 3.run app
print("runing app")
if __name__ == "__main__":
    app.run(debug=True)
    # listening