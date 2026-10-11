from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My Flask server is working!"

@app.route("/about")
def about():
    return "This is my About page!"

@app.route("/about")
def about():
    return "This is my About page!"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/api")
def api():
    return jsonify({
        "name": "Melly",
        "course": "Flask",
        "level": "beginner"
    })


if __name__ == "__main__":
    app.run(debug=True)