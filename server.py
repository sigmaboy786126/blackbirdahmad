from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search():
    username = request.args.get("username")
    email = request.args.get("email")

    if not username and not email:
        return jsonify({"error": "Please provide username or email"}), 400

    cmd = ["python", "blackbird.py"]
    if username:
        cmd += ["--username", username]
    if email:
        cmd += ["--email", email]

    result = subprocess.run(cmd, capture_output=True, text=True)
    return jsonify({"output": result.stdout})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
