from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Read footer text from environment variable
FOOTER_TEXT = os.getenv("FOOTER_TEXT", "Mohammed Aatef, Elevate Labs – Intern")

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        name = request.form.get("name")
        message = f"Congrats {name}! You successfully deployed a containerized application. 🎉"
    return render_template("index.html", message=message, footer_text=FOOTER_TEXT)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
