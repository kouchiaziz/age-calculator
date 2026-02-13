from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DB_NAME = "database.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/posts", methods=["GET"])
def get_posts():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM posts ORDER BY id DESC")
    posts = [{"id": row[0], "content": row[1]} for row in c.fetchall()]
    conn.close()
    return jsonify(posts)

@app.route("/posts", methods=["POST"])
def add_post():
    data = request.json
    content = data.get("content")
user = data.get("user", "طالب")

posts.append({
    "id": len(posts) + 1,
    "content": content,
    "user": user
})


    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO posts (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Post added"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
