import urllib.request
import gevent
from gevent import monkey
import re

monkey.patch_all()


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg", 'https://rpic.douyucdn.cn/live-cover/appCovers/2020/01/28/5515841_20200128025400_small.jpg'),
        gevent.spawn(downloader, "2.jpg", 'https://rpic.douyucdn.cn/live-cover/appCovers/2020/02/13/3311650_20200213193746_small.jpg')
    ])


if __name__ == '__main__':
    main()
