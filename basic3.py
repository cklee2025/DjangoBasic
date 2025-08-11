# 세부적인 요청 처리를 위해 
# http.client 모듈 사용 : GET 방식 
from http.client import HTTPConnection
host = 'www.example.com'
conn = HTTPConnection(host)
conn.request('GET', '/')
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
# 일부만 읽는 경우
# data1 = r1.read(100)
# 두번째 요청에 대한 테스트
conn.request('GET', '/')
r2 = conn.getresponse()
print(r2.status, r2.reason)
data2 = r2.read()
print(data2.decode())
conn.close()


# http.client  모듈 사용 : POST 방식 
from http.client import HTTPConnection
from urllib.parse import urlencode
host = '127.0.0.1:8000'
params = urlencode({
    'language': 'python',
    'name': '김석훈',
    'email': 'shkim@naver.com',
})
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/plain',
}
conn = HTTPConnection(host)
conn.request('POST', '/', params, headers)
resp = conn.getresponse()
print(resp.status, resp.reason)
data = resp.read()
print(data.decode('utf-8'))
conn.close()


# http.client 모듈 활용 : 
# 특정 웹 사이트의 이미지들을 내려받는 프로그램  
from pathlib import Path
from http.client import HTTPConnection
from urllib.parse import urljoin, urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser
class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)
def download_image(url, data):
    downDir = Path('DOWNLOAD')
    downDir.mkdir(exist_ok=True)
    parser = ImageParser()
    parser.feed(data)
    dataSet = set(x for x in parser.result)

    for x in sorted(dataSet) :
        imageUrl = urljoin(url, x)
        basename = Path(imageUrl).name
        targetFile = downDir / basename

        print("Downloading...", imageUrl)
        urlretrieve(imageUrl, targetFile)
        
def main():
    host = "www.google.co.kr"
    conn = HTTPConnection(host)
    conn.request("GET", '')
    resp = conn.getresponse()

    charset = resp.msg.get_param('charset')
    data = resp.read().decode(charset)
    conn.close()

    print("\n>>>>>>>>> Download Images from", host)
    url = urlunparse(('http', host, '', '', '', ''))
    download_image(url, data)

if __name__ == '__main__':
    main()
