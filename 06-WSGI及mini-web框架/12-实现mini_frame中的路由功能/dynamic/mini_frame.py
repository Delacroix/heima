import re


def index():
    # 如果以web_server.py启动，则文件相对路径都是以web_server.py计算
    with open("./templates/index.html") as f:
        content = f.read()

    my_stock_info = "这是你的本月名称..."
    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content


def center():
    with open("./templates/center.html") as f:
        content = f.read()

    my_stock_info = "这是从mysql查询的..."
    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content



URL_FUNC_DICT = {
    "/index.py": index,
    "/center.py": center
}


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

    func = URL_FUNC_DICT[file_name]
    return func()