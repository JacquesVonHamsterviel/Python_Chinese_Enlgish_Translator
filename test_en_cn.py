import requests

url='http://127.0.0.1:5690/report'
while True:
    text=input("Text: ")
    data={'text':text,'lan':'en'}
    r=requests.post(url,data)
    print(r.content.decode('utf-8'))