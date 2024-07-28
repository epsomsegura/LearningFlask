from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Main python ready"


if __name__ == "__main__":
    app.run()
