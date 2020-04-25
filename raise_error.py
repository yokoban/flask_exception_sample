class MyError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = kwargs["message"]
        self.code = kwargs["code"]


def raise_my_error(code):
    raise MyError(code=code, message=f"ERROR CODE: {code}")


def raise_other_error(code):
    raise FileNotFoundError("ファイルが見つかりませんでした。", code)
