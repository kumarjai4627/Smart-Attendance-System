from flask import Flask, render_template
from config import Config
from database.db import mysql

app = Flask(__name__)
app.config.from_object(Config)

mysql.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/testdb")
def testdb():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        cur.close()
        return f"MySQL Connected Successfully! Version: {version[0]}"
    except Exception as e:
        return f"Database Connection Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)