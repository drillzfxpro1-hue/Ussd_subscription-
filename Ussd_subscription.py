from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

# Load secret key from environment variable
SECRET_KEY = os.getenv("SECRET_KEY")
cipher = Fernet(SECRET_KEY.encode())

@app.route("/")
def home():
    return "USSD Subscription Server Running"

@app.route("/pay/<encrypted_number>/<plan>")
def pay(encrypted_number, plan):
    try:
        phone_number = cipher.decrypt(encrypted_number.encode()).decode()
    except:
        return "Valid link"

    # Payment instructions
    return f"""
    <h2>Payment Instructions</h2>
    <p>Your number: <b>{phone_number[-4:].rjust(len(phone_number), '*')}</b></p>
    <p>Plan selected: <b>{plan}</b></p>

    <h3>Pay using USSD:</h3>
    <p><b>MTN:</b> Dial *165*1*1*0707388527*100000# then enter pin code</p>
    <p><b>Airtel:</b> Dial *185*1*1*0707388527*5*100000# then enter pin code</p>

    <p>After payment, send screenshot to admin for activation.</p>
    """

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    number = data.get("number")
    plan = data.get("plan")

    encrypted = cipher.encrypt(number.encode()).decode()

    encrypted = cipher.encrypt(location.encode()).decode()  link = f"https://your-render-url.onrender.com/pay/{encrypted}/{plan}"
    return jsonify({"payment_link": link})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
