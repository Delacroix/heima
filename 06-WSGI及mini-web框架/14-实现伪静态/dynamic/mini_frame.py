import re

"""
URL_FUNC_DICT = {
    "/index.py": index,
    "/center.py": center
}
"""

URL_FUNC_DICT = dict()

# 实现一个带参数的装饰器，将URL作为参数进行传递，实现路由
def route(url):
    def set_func(func):
        # 等同于 URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route("/index.html")
def index():
    # 如果以web_server.py启动，则文件相对路径都是以web_server.py计算
    with open("./templates/index.html") as f:
        content = f.read()

    my_stock_info = "这是你的本月名称..."
    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content


@route("/center.html")
def center():
    with open("./templates/center.html") as f:
        content = f.read()

    my_stock_info = "这是从mysql查询的..."
    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    # file_name = '/index.py'

    """
    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return 'Hello World! 我爱你中国···'
    """

    try:
        func = URL_FUNC_DICT[file_name]
        return func()
    except Exception as ret:
        return "产生了异常: %s" % str(ret)