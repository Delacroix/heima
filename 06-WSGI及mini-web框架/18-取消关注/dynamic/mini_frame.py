import re
from pymysql import connect

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
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        # 等同于 URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route(r"/index.html")
def index(ret):
    # 如果以web_server.py启动，则文件相对路径都是以web_server.py计算
    with open("./templates/index.html") as f:
        content = f.read()

    # try:
    #     file_name = file_name.replace(".py", ".html")
    #     f = open(template_root + file_name)
    # except Exception as ret:
    #     return "%s" % ret
    # else:
    #     content = f.read()
    #     f.close()

    # my_stock_info = "这是你的本月名称..."
    # content = re.sub(r"\{%content%\}", my_stock_info, content)
    conn = connect(host='192.168.211.131',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cs = conn.cursor()
    cs.execute("select * from info;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    html_template = """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
        </td>
    </tr>
    """

    html = ""
    for info in stock_infos:
        html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[1])

    content = re.sub(r"\{%content%\}", html, content)

    return content


@route("/center.html")
def center(ret):
    with open("./templates/center.html") as f:
        content = f.read()
    # my_stock_info = "这是从mysql查询的..."
    # content = re.sub(r"\{%content%\}", my_stock_info, content)
    conn = connect(host='192.168.211.131',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cs = conn.cursor()
    cs.execute("SELECT i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i INNER JOIN focus as f on i.id=f.info_id;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
 
 
    html_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
            </td>
        </tr>
        """

    html = ""

    for info in stock_infos:
        html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[0], info[0])

    content = re.sub(r"\{%content%\}", html, content)

    return content


# 给路由添加正则表达式的原因：在实际开发时，url中往往会带有很多参数，例如/add/000007.html中000007就是参数，
# 如果没有正则的话，那么就需要编写N次@route来进行添加 url对应的函数 到字典中，此时字典中的键值对有N个，浪费空间
# 而采用了正则的话，那么只要编写1次@route就可以完成多个 url例如/add/00007.html /add/000036.html等对应同一个函数，此时字典中的键值对个数会少很多
@route(r"/add/(\d+)\.html")
def add_focus(ret):
    # 1.获取股票代码
    stock_code = ret.group(1)
    # 2.判断是否有这个股票代码
    conn = connect(host='192.168.211.131',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cs = conn.cursor()
    sql = """select * from info where code = %s;"""
    cs.execute(sql, (stock_code,))

    # 如果没有这个股票代码，则认为时非法请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这支股票"

    # 3.判断是否已经关注过
    sql = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, stock_code)
    # 如果查出来了，表示已经关注过
    if cs.fetchone():
        return "已经关注过了，请勿重复关注"

    # 4.添加关注
    sql = """insert into focus (info_id) select id from info where code=%s;"""
    cs.execute(sql, stock_code)
    conn.commit()
    cs.close()
    conn.close()
    return "关注成功:%s" % stock_code


@route(r"/del/(\d+)\.html")
def del_focus(ret):
    # 1.获取股票代码
    stock_code = ret.group(1)
    # 2.判断是否有这个股票代码
    conn = connect(host='192.168.211.131',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cs = conn.cursor()
    sql = """select * from info where code = %s;"""
    cs.execute(sql, (stock_code,))

    # 如果没有这个股票代码，则认为时非法请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这支股票"

    # 3.判断是否已经关注过
    sql = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, stock_code)
    # 如果没有关注过，表示非法请求
    if not cs.fetchone():
        return "%s 没有关注过，请勿取消操作" % stock_code

    # 4.取消关注
    sql = """delete from focus where info_id = (select id from info where code=%s);"""
    cs.execute(sql, stock_code)
    conn.commit()
    cs.close()
    conn.close()
    return "取消关注成功:%s" % stock_code


@route(r"/update/\d+\.html")
def show_update_page(ret):
    """显示修改的页面"""
    with open("./templates/update.html") as f:
        content = f.read()

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

    # try:
    #     func = URL_FUNC_DICT[file_name]
    #     return func()
    # except Exception as ret:
    #     return "产生了异常: %s" % str(ret)
    
    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        # return URL_FUNC_DICT[file_name]()
        for url, func in URL_FUNC_DICT.items():
            # {
            #   r"/index.html":index,
            #   r"/center.html":center,
            #   r"/add/\d+\.html":add_focus
            # }
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else:
            return "请求的url(%s)没有对应的函数...." % file_name


    except Exception as ret:
        return "产生了异常：%s" % str(ret)