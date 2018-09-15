from flask import Flask
app = Flask(__name__)
Books = {
    "giatuvukhi":
    {        "Name" : "A Farewell to Arms",        "Age" : 89,        "Genre" : "Literary realism",    },
    "haisophan":
    {        "Name" : "Kane and Abel",        "Age" : 39,        "Genre" : "Novel",       },
    "motminhtrongrung":
    {        "Name" : "Walden",        "Age" : 164,        "Genre" : "Memoir"    },
}

@app.route("/user/<username>")
def book(username):
    if username in Books.keys():
        return (str(Books[username]))
    else:
        return "not found"

print("runing app")
if __name__ == "__main__":
    app.run(debug=True)