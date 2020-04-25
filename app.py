from flask import Flask, abort, jsonify
from raise_error import MyError, raise_my_error, raise_other_error

app = Flask(__name__)


# 独自例外MyErrorをエラーハンドラーとして登録して処理を行う
@app.errorhandler(MyError)
def halder_usage(my_error):
    return f"code: {my_error.code}, message: {my_error.message}"


# 通常の例外を処理する
@app.errorhandler(Exception)
def handler_normal_usage(other_error):
    # other_errorに詰め直されたエラーが渡される
    # other_error.argsにタプルとして入ってくる
    error = {"code": other_error.args[0], "message": other_error.args[1]}

    return jsonify(error)


# 独自例外(MyError)を発生させる
@app.route("/my")
def my_error():
    raise_my_error(400)

    return "my error"


# 独自例外(MyError)を発生させtryでErrorをキャッチする
@app.route("/my/try")
def my_try_error():
    try:
        raise_my_error(400)
    except MyError as e:
        # MyErrorで送られてきたcode, messagewpExceptionに入れ直す
        # このときExceptionは名前付き引数を理解しないので位置引数として渡す
        raise Exception(e.code, e.message)


# 通常の例外を発生させる
@app.route("/other")
def other_error():
    raise_other_error("500")

    return "other error"


if __name__ == "__main__":
    app.run(debug=True)
