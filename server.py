from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    if request.args.get('hex') == "vbhjgjlhl":
        return "6G6rwTYL"

app.run(debug=False, port=1003)