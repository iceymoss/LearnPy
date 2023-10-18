from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello, world!"


@app.route("/my_info/<user_name>")
def my_info(user_name):
    return {"name": user_name, "age": 18}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
