import re


def main():
    content_jd = """
    <div class="job-detail">
        <p>工作内容：</p>
<p>参与糗事百科的后端研发；</p>
<p>保障产品的快速迭代与服务质量；</p>
<p>任职资格：</p>
<p>三年以上高并发系统的设计与调优经验，对系统的架构与实现有清晰的认识；</p>
<p>熟悉linux系统生产环境搭建与调优；</p>
<p>至少熟悉 Python/Golang/C/C++ 其中一种语言</p>
<p>熟练掌握Mysql数据库的使用与优化；</p>
<p>熟悉至少一种web框架的使用和调优，并了解其基本原理</p>
<p>扎实的编程功底，能享受编程乐趣；</p>
<p>高效的学习能力和分析解决问题能力；</p>
<p>本科及以上学历；</p>
<p><br></p>
<p>加分项：有团队管理经验，团队驱动力者优先~ ~</p>
        </div>
    """

    ret = re.sub(r"<[^>]*>|\n|\s", "", content_jd)
    print(ret)


if __name__ == '__main__':
    main()
