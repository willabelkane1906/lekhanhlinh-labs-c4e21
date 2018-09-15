from flask import Flask, render_template, redirect
app = Flask(__name__)
@app.route("/aboutme")
def homepage():
    return render_template("aboutme.html")

@app.route("/school")
def techkid():
    return redirect("http://techkids.vn" , code=302 )

print("runing app")
if __name__ == "__main__":
    app.run(debug=True)