from flask import Flask, render_template
from config import Config
from database.db import mysql

from routes.student import student_bp
from routes.auth import auth_bp

app = Flask(__name__)

app.config.from_object(Config)

# Secret Key (Session ke liye)
app.secret_key = "smart_attendance_secret_key"

# MySQL Initialize
mysql.init_app(app)

# Blueprints
app.register_blueprint(student_bp)
app.register_blueprint(auth_bp)


from flask import Flask, render_template, redirect, url_for
@app.route("/")
def home():
    return redirect(url_for("auth.login"))

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