from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from CI/CD Pipeline 🚀</h1>
    <h2>GitHub + Jenkins + Docker + Ansible</h2>
    <p>Deployment Successfully Done With Automation Only!</p>
    <p>Done by CICD!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
