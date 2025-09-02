from flask import Flask
import os, psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "admin"),
            password=os.getenv("DB_PASSWORD", "admin123"),
            dbname=os.getenv("DB_NAME", "testdb"),
            connect_timeout=3
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return "OK: Flask connected to PostgreSQL ✅"
    except Exception as e:
        return f"ERROR DB ❌: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
