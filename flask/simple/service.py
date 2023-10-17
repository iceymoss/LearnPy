from flask import Flask, Blueprint

index_page = Blueprint("index_page", __name__)


@index_page.route("/hello")
def hello():
    return "hello, flask"


@index_page.route("/user_info")
def get_user():
    return {"name":"iceymoss", "age": 18}
