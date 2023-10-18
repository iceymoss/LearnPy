
from flask import Flask, Blueprint, render_template, make_response, jsonify

index_page = Blueprint("index_page", __name__)


@index_page.route("/index")
def index():
    user_info = {"name": "蔡徐坤", "age": "28", "live": "ShangHai", "Skill": ["唱", "跳", "rap", "篮球"], "Features":["ban小黑子", "你干嘛呢哎呦", "🐔霓太美"]}
    return render_template("index.html", user=user_info)


@index_page.route("/extend_template")
def extend():
    return render_template("extend_template.html")


@index_page.route("/get_course")
def get_course():
    import database
    sql = "select * from course_infos"
    database.db_connection.execute(sql)

    # 获取查询结果
    result = database.db_connection.fetchall()

    res = []
    # 处理结果数据
    for row in result:
        print(row)
        res.append(str(row))
    data = {"code":0, "msg":{"list":res, "total": len(res)}}
    response = make_response(jsonify(data))
    return response



