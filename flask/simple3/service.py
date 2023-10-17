from flask import Flask, Blueprint, render_template

index_page = Blueprint("index_page", __name__)


@index_page.route("/index")
def index():
    user_info = {"name": "iceymoss", "age": "18", "live": "ShangHai"}
    return render_template("index.html", name=user_info)
