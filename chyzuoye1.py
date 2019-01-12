import urllib.request  # Python的基础爬虫库，后面不会用,但是必须要会！！！
import urllib.parse
def main():
    headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    request = urllib.request.Request('http://www.17k.com/chapter/2933095/36699279.html')
    response = urllib.request.urlopen(request)
    jg=response.read().decode('utf8')
    print(jg)
    with open("/home/chy/Desktop/chy/test1.txt",mode='w') as f:
    f.write(jg)
main()