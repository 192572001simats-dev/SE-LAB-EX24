from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "SE Lab Experiment 24 - Flask Application"

@app.route("/test")
def test():
    return "Application is working successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)