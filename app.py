from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for "/"
@app.route("/notification-service/")
def home():
    return "<h2>Welcome to the MediTrack - Notification Service! <h2>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
