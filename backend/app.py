from flask import Flask, request, jsonify
from database import cursor, db
from resume_parser import extract_text
from ranking import rank

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    data = request.form
    cursor.execute(
        "INSERT INTO users(name,email,password,role) VALUES(%s,%s,%s,%s)",
        (data["name"],data["email"],data["password"],data["role"])
    )
    db.commit()
    return "Registered Successfully"

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    cursor.execute("SELECT role FROM users WHERE email=%s AND password=%s",(email,password))
    user = cursor.fetchone()
    return "Login Successful" if user else "Invalid"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["resume"]
    text = extract_text(file)
    scores = rank(text)
    return jsonify(scores)

@app.route("/chart-data")
def chart():
    return jsonify({
        "labels":["Web","AI","Data"],
        "values":[80,60,70]
    })

@app.route("/admin-data")
def admin():
    cursor.execute("SELECT * FROM users")
    return jsonify(cursor.fetchall())

app.run(debug=True)
