from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Quntom Migration Dashboard</h1>
    <p>Hybrid Adaptive Migration Framework</p>
    <p>System Status: Active</p>
    """

if __name__ == "__main__":
    app.run(debug=True)