from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/file/<filename>")
def serve_files(filename):
    if os.path.exists(filename):
        return send_file(filename)
    return "File not found", 404

@app.route("/api")
def api_response():
    if os.path.exists("opacity.txt"):
        with open("opacity.txt", "r") as f:
            opacity = round(float(f.read().strip()), 2)

        new_opacity = opacity - 0.05
        with open("opacity.txt", "w") as f:
            f.write(str(new_opacity))

        return jsonify(opacity), 200
    return "Could not Reach API", 404
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80 ,debug=True)