from sentiment import analysis
from getcomment import getcomment
from flask import Flask, render_template, request, abort

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analysis", methods=["POST"])
def main():
    url = request.form["url"]
    comments, status = getcomment(url)
    if status == 1:
        abort(404)
    elif status == 0:
        # print(comments)
        return render_template("analysis.html", data=analysis(comments))


@app.route("/help")
def help():
    return render_template("site/index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
