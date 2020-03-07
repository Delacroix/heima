def index():
    # 如果以web_server.py启动，则文件相对路径都是以web_server.py计算
    with open("./templates/index.html") as f:
        content = f.read().encode('utf-8')
    return content


def center():
    with open("./templates/center.html") as f:
        content = f.read().encode('utf-8')
    return content


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    # file_name = '/index.py'

    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return 'Hello World! 我爱你中国···'
