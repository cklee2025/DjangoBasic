import urllib.request
print(urllib.request.urlopen("http://www.example.com").read().decode('utf-8'))


from urllib.request import urlopen
f = urlopen("http://www.example.com")
print(f.read(500).decode('utf-8'))


from urllib.request import urlopen
data = "language=python&framework=django"
f = urlopen("http://127.0.0.1:8000", bytes(data, encoding='utf-8'))
print(f.read().decode('utf-8'))


# 요청을 보낼 때 요청 헤더를 지정하고 싶을 경우. 
# url 지정 방식을 변경, url 인자에 Request 객체 지정
from urllib.request import urlopen, Request
from urllib.parse import urlencode
url = 'http://127.0.0.1:8000'
data = {
    'name': '김석훈',
    'email': 'shkim@naver.com',
    'url': 'http://www.naver.com',
}
encData = urlencode(data)
postData = bytes(encData, encoding='utf-8')
req = Request(url, data=postData)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
f = urlopen(req)
print(f.headers)
print(f.read(500).decode('utf-8'))


# urllib.request 모듈에서 정의된 HTTPBasicAuthHandler 클래스를 사용하여 
# 인증데이터를 같이 보내는 프로그램
from urllib.request import HTTPBasicAuthHandler, build_opener
auth_handler = HTTPBasicAuthHandler()
auth_handler.add_password(realm='ksh', user='shkim', passwd='shkimadmin', 
                          uri='http://127.0.0.1:8000/auth/')
opener = build_opener(auth_handler)
resp = opener.open('http://127.0.0.1:8000/auth/')
print(resp.read().decode('utf-8'))


# urllib.request 모듈에서 정의된 HTTPCookieProcessor 클래스를 사용하여 
# 쿠키 데이터를 같이 처리하는 프로그램
from urllib.request import Request, HTTPCookieProcessor, build_opener
url = 'http://127.0.0.1:8000/cookie/'
# first request (GET) with cookie handler
# 쿠키 핸들러 생성, 쿠키 데이터 저장은 디폴트로 CookieJar 객체를 사용함
cookie_handler = HTTPCookieProcessor()
opener = build_opener(cookie_handler)
req = Request(url)
resp = opener.open(req)
print("< first Response after GET Request > \n")
print(resp.headers)
print(resp.read().decode('utf-8'))

# second request (POST) with Cookie header
print("-------------------------------------------------------")
data = "language=python&framework=django"
encData = bytes(data, encoding='utf-8')
req = Request(url, encData)
resp = opener.open(req)
print("< second Response after POST Request > \n")
print(resp.headers)
print(resp.read().decode('utf-8'))



