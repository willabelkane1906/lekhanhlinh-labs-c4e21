from flask import Flask, render_template, request
import mlab
app = Flask(__name__)
mlab.connect()

@app.route("/register", methods=["GET", "POST"])
def id():
    if request.method == "GET":
        return render_template("ex1.html")
    elif request.method == "POST":
       
        form = request.form
        fullname = form["fullname"]
        email = form["email"]
        username = form["username"]
        password = form["password"]
        

        new_id = Post(fullname=fullname, email=email, username=username, password=password)
        new_id.save()
        return "OK"
 


if __name__ == "__main__":
    app.run(debug=True)
