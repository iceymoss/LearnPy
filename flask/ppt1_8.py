from flask import Flask, Blueprint

app = Flask(__name__)

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def hello():
    return "hello, flask"


app.register_blueprint(index_page, url_perfix="/my_info")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
