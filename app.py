from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def insert():
    return "This is schedule api."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
