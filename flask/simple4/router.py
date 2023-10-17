from flask import Flask
from service import index_page

app = Flask(__name__)

app.register_blueprint(index_page, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
