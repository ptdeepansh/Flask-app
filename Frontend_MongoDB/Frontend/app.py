from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return '<span style="display:flex; justify-content:center">Welcome to simple Flask Application!!</span>'


@app.route("/html")
def show():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(
        host="127.1.0.1",
        port=9070,
        debug=True
    )
