from flask import Flask, Blueprint, request, make_response, jsonify, render_template

index_page = Blueprint("index_page", __name__)


@index_page.route("/hello")
def hello():
    return "hello, flask"


@index_page.route("/user_info")
def get_user():
    return {"name": "iceymoss", "age": 18}


@index_page.route("/add")
def get_good():
    var_a = request.args.get("a", 0)
    var_b = request.args.get("b", 0)
    return "计算结果：{0}".format(int(var_b) + int(var_a))


@index_page.route("/login", methods=["POST"])
def loging():
    user_name = request.form["user_name"]
    password = request.form["password"]
    if user_name == "iceymoss" and password == "admin123":
        return {"code": 0, "msg": "", "token": "difhdanf3rudifndf.dfrhindfidf89er.49fhdigjaihg8qa"}

    return "用户名称或密码不正确"


@index_page.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"] if "file" in request.files else None
    return "request: %s, params: %s, file:%s" % (request.method, request.files, f)


@index_page.route("/text_same")
def text_same():
    response = make_response("text/html", 200)
    return response


@index_page.route("/json")
def json():
    import json
    user_info = {"name": "iceymoss", "age": 18, "live": "ShangHai"}
    response = make_response(json.dumps(user_info))
    response.headers["Content-Type"] = "application/json"
    return response


@index_page.route("/json_test")
def json_test():
    user_info = {"name": "iceymoss", "age": "18", "live": "ShangHai"}
    response = make_response(jsonify(user_info))
    return response


@index_page.route("/index")
def index():
    return render_template("index.html", name=name)
