from flask import Flask, Blueprint, render_template

index_page = Blueprint("index_page", __name__)


@index_page.route("/index")
def index():
    user_info = {"name": "蔡徐坤", "age": "28", "live": "ShangHai", "Skill": ["唱", "跳", "rap", "篮球"], "Features":["ban小黑子", "你干嘛呢哎呦", "🐔霓太美"]}
    return render_template("index.html", user=user_info)

@index_page.route("/extend_template")
def extend():
    return render_template("extend_template.html")
