from pymysql import *


def main():
    conn = connect(host='localhost', port=3306, user='root', password='mysql', database='jing_dong', charset='utf8')
    cs1 = conn.cursor()
    count = cs1.execute('select id,name from goods where id>=4')
    print("查询到%d条数据:" % count)

    for i in range(count):
        # 获取查询的结果
        result = cs1.fetchone()
        # 打印查询的结果
        print(result)
        # 获取查询的结果

    # 关闭Cursor对象
    cs1.close()


if __name__ == '__main__':
    main()