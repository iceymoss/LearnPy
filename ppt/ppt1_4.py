from flask import Flask

app = Flask(__name__)
app.config.from_object("config.base_setting")
@app.route("/")
def hello():
    return "hello, world!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)