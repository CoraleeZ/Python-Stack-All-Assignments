from flask import Flask, render_template,request
from mysqlconn import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL("friendship")
    friends = mysql.query_db("SELECT * FROM friendships;")
    print(friends)
    return render_template("index.html", all_friends = friends)


@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    print(request.form)

if __name__ == "__main__":
    app.run(debug=True)
