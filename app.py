from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7698602745:AAFMv5XvD0OVfiYxPiLD94IOJI9IS0dpewg'
CHAT_ID = '-4949237168'

@app.route('/receive-alarm', methods=['POST'])
def receive_alarm():
    data = request.json
    alarm = data.get('alarmName', 'Unknown Alarm')
    severity = data.get('severity', 'Unknown')
    description = data.get('description', '')

    message = f"🚨 [{severity}] {alarm}\n{description}"
    telegram_url = f"https://api.telegram.org/bot7698602745:AAFMv5XvD0OVfiYxPiLD94IOJI9IS0dpewg/sendMessage"
    requests.post(telegram_url, json={"chat_id": CHAT_ID, "text": message})
    return 'OK'