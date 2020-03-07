from pymysql import *
import re


class JD(object):
    def __init__(self):
        # 创建Connection连接
        self.conn = connect(host='localhost', port=3306, user='root', password='mysql', database='jing_dong',
                            charset='utf8')
        # 获得cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭cursor对象
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        """显示所有的商品"""
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        """显示所有分类"""
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def show_brand(self):
        """显示所有品牌分类"""
        sql = "select name from goods_brands;"
        self.execute_sql(sql)

    def add_brand(self):
        """添加品牌分类"""
        item_name = input("输入新商品品牌的名称:")
        sql = """insert into goods_brands (name) values("%s")""" % item_name
        self.execute_sql(sql)
        self.conn.commit()

    def get_info_by_name(self):
        find_name = input("请输入要查询的商品名称:")
        # sql = """select * from goods where name='%s'""" % find_name
        # print("--->%s<---" % sql)
        # self.execute_sql(sql)
        sql = "select * from goods where name = %s"
        self.cursor.execute(sql, [find_name])
        print(self.cursor.fetchall())

    def user_register(self):
        user_name = input("请输入需要注册的用户名:")
        user_password = input("请输入密码:")
        user_address = input("请输入收货地址:")
        user_cellphone = input("请输入联系电话:")
        sql = """insert into customer values(0, '%s', '%s', '%s', '%s');""" % (user_name, user_password, user_address,
                                                                               user_cellphone)
        print("注册成功！%s" % user_name)
        self.execute_sql(sql)
        self.conn.commit()

    def user_login(self):
        user_name = input("请输入用户名:")
        user_password = input("请输入密码:")
        sql = """select passwd from customer where name in (select name from customer where name = %s) and passwd = %s"""
        result = self.cursor.execute(sql, ([user_name], [user_password]))
        print(self.cursor.fetchall())
        print(result)
        if result == 1:
            print("登录成功，欢迎选购，%s !" % user_name)
        else:
            print("用户名或密码错误")

    def user_order(self):
        order_goods_name = input("请输入想要购买的商品:")
        order_goods_qutity = input("请输入想要购买的数量:")
        # fetch_time = "select now()"
        # sql = """insert into order_detail values(0, %d, ) """
        # self.execute_sql(sql)

        # print(self.cursor.fetchall())
        # price_raw = str(self.cursor.fetchall())
        # print(re.findall(r"\d+\.\d+", price_raw))

    @staticmethod
    def print_menu():
        print("---京东商城---")
        print("1: 所有的商品")
        print("2: 所有的商品分类")
        print("3: 所有的商品品牌分类")
        print("4: 添加一个商品分类")
        print("5: 根据名字查询一个商品")
        print("6: 注册用户")
        print("7: 用户登录")
        # print("8: 用户下订单")
        num = input("请输入功能对应的序号：")
        return num

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                # 查询所有商品
                self.show_all_items()
            elif num == "2":
                # 查询分类
                self.show_cates()
            elif num == "3":
                # 查询品牌分类
                self.show_brand()
            elif num == "4":
                # 添加品牌
                self.add_brand()
            elif num == "5":
                # 根据名字查询商品
                self.get_info_by_name()
            elif num == "6":
                # 用户注册
                self.user_register()
            elif num == "7":
                # 用户登录
                self.user_login()
            # elif num == "8":
            #     # 用户下订单
            #     self.user_order()
            else:
                print("输入有误，重新输入...")


def main():
    # 1.创建一个京东商城对象
    jd = JD()
    # 2.调用这个对象的run方法，让其运行
    jd.run()


if __name__ == '__main__':
    main()
