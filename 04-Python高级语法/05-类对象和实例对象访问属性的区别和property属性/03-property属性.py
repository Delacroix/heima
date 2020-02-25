# ############### 定义 ###############
class Pager:
    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


# ############### 调用 ###############
p = Pager(1)
print("起始物品ID为%s" % p.start)  # 就是起始值，即：m
print("结束物品ID为%s" % p.end)  # 就是结束值，即：n

# Python的property属性的功能是：property属性内部进行一系列的逻辑计算，最终将计算结果返回。
