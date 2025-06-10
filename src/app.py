from flask import Flask, request, jsonify
import qrcode
import os
import pymysql

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_NAME = os.getenv("DB_NAME", "qr_code_db")

@app.route("/generate", methods=["POST"])
def generate_qr():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    url = data.get("redirect_url")
    client_id = data.get("id_cliente")

    if not url or not client_id:
        return jsonify({"error": "Missing redirect_url or id_cliente"}), 400

    qr_img = qrcode.make(url)
    image_path = f"static/qr_{client_id}.png"
    os.makedirs("static", exist_ok=True)
    qr_img.save(image_path)

    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO qr_codes (redirect_url, id_cliente, image_url) VALUES (%s, %s, %s)",
            (url, client_id, image_path)
        )
        conn.commit()

    return jsonify({"message": "QR code created", "image_url": image_path})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
