# "실습 생략": Proxy Server 없으므로 ...

import urllib.request
url = 'http://www.example.com'
proxyServer = 'http://www.proxy.com:3128/'
# 프록시 서버를 통해 웹서버로 요청을 보냅니다.
proxy_handler = urllib.request.ProxyHandler({'http': proxyServer})
# 프록시 서버 설정을 무시하고 웹 서버로 요청을 보냅니다.
# proxy_handler = urllib.request.ProxyHandler({})
# 프록시 서버에 대한 인증을 처리합니다.
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# 2개의 핸들러를 오프너에 등록합니다.
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# 디폴트 오프너로 지정하면 urlopen() 함수로 요청을 보낼 수 있습니다.
urllib.request.install_opener(opener)
# opener.open() 대신에 urlopen()을 사용하였습니다.
f = urllib.request.urlopen(url)
print("geturl():", f.geturl())
print(f.read(300).decode('utf-8'))


# 특정 웹 사이트에서 이미지만을 검색 그 리스트 조회 
# 실행 방법 : 실행 범위 line 선택 후 :  run selection/line in interactive wondows
from urllib.request import urlopen
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
def parse_image(data):
    parser = ImageParser()
    parser.feed(data)
    dataSet = set(x for x in parser.result)
    return dataSet
def main():
    url = "http://www.google.co.kr"
    with urlopen(url) as f:
        charset = f.info().get_param('charset')
        data = f.read().decode(charset)
    dataSet = parse_image(data)
    print("\n>>>>>>>>> Fetch Images from", url)
    print('\n'.join(sorted(dataSet)))
if __name__ == '__main__':
    main()




