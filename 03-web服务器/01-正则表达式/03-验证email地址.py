import re


def main():
    email = input("请输入一个邮箱地址:")
    # 如果在正则表达式中用到了某些预留的字符，比如 . ?等，需要在他们之前添加 \ 用于转义
    ret = re.match(r"^[a-zA-Z0-9_]{4,20}@163\.com$", email)
    if ret:
        print("%s 符合要求" % email)
    else:
        print("%s 不符合要求" % email)


if __name__ == '__main__':
    main()
