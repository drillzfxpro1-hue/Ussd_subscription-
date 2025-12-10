from flask import Flask, request, jsonify

app = Flask(__name__)

# This will store subscriber payment records in memory for now
subscribers = {}

@app.route("/")
def home():
    return "USSD Subscription Server is running!"

@app.route("/activate", methods=["POST"])
def activate():
    data = request.get_json()
    phone = data.get("phone")
    code = data.get("code")

    if not phone or not code:
        return jsonify({"status": "error", "message": "Missing phone or code"}), 400

    subscribers[phone] = code

    return jsonify({"status": "success", "message": "Subscription activated", "phone": phone})


@app.route("/verify/<phone>", methods=["GET"])
def verify(phone):
    if phone in subscribers:
        return jsonify({"status": "active", "code": subscribers[phone]})

    return jsonify({"status": "not_active"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
