import urllib.request  # Python的基础爬虫库，后面不会用,但是必须要会！！！
import urllib.parse
def fm(gjz):
    headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    parameters = {
        "wd":gjz,
    }
    data =  urllib.parse.urlencode(parameters)
    print(data)
    request_ = urllib.request.Request(url='http://www.baidu.com/s?'+data
    ,method="GET")
    response=urllib.request.urlopen(request_)
    print(response.url)
    HTML=response.read().decode()
    print(HTML)
    with open("/home/chy/Desktop/chy/test.txt",mode='w') as f:
        f.write(HTML)
fm("huwangshihaoren")