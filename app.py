from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate encryption key (keep this safe)
key = Fernet.generate_key()
cipher = Fernet(key)

# Your secret number but encrypted
original_number = "256700123456"
encrypted_number = cipher.encrypt(original_number.encode()).decode()

@app.route("/")
def home():
    return "Payment Verification Server Running"

@app.route("/pay", methods=["POST"])
def pay():
    user_id = request.form.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user ID"}), 400

    # Fake payment confirmation (you will replace this later)
    return jsonify({
        "status": "success",
        "message": "Payment processed",
        "verification_code": "VIP-" + user_id[-4:],
        "encrypted_contact": encrypted_number
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
