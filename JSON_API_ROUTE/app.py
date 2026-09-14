from flask import Flask, send_file, abort
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "JSON API Route Home"

@app.route("/api", methods=['GET'])
def API():

    filepath = "/home/deepanshu/DevOps/Assign3/JSON_API_ROUTE/test.json"

    if not os.path.exists(filepath):
        abort(404, "File not found")

    else:
        return send_file(
            filepath, 
            as_attachment=False)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9010, debug=True)