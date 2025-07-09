from flask import Flask, request, jsonify
import datetime
import requests

app = Flask(__name__)

# ==========================
# 1. Endpoint รับ token (mock auth)
# ==========================
@app.route("/api/get-token", methods=["POST"])
def get_token():
    data = request.json
    if data["userName"] == "Tewit" and data["value"] == "Tewit160946":
        return {"token": "mock-token-123"}
    else:
        return {"error": "Unauthorized"}, 401

# ==========================
# 2. Endpoint รับ Alarm/Event จาก iMaster NCE
# ==========================
@app.route("/receive-alarm", methods=["POST"])
def receive_alarm():
    data = request.json
    print("🔔 Alarm/Event received:", data)

    # สร้างข้อความส่ง Telegram (หากใช้)
    msg = f"📡 [NCE Alarm/Event]\n\n{data}"

    # ส่งข้อความไปยัง Telegram (ถ้าคุณเชื่อม bot ไว้แล้ว)
    telegram_bot_token = "7698602745:AAFMv5XvD0OVfiYxPiLD94IOJI9IS0dpewg"
    chat_id = "-4949237168"
    telegram_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": "HTML"
    }
    try:
        r = requests.post(telegram_url, json=payload)
        print("✅ Telegram status:", r.status_code)
    except Exception as e:
        print("❌ Telegram Error:", e)

    return jsonify({"status": "ok"}), 200

# ==========================
# 3. Root Check (เช็คว่า Flask รันอยู่)
# ==========================
@app.route("/", methods=["GET"])
def index():
    return f"iMaster Webhook Online: {datetime.datetime.now()}", 200

# ==========================
# Run the Flask app
# ==========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)