import requests

r = requests.get('https://www.cnblogs.com/')
print(r.status_code)

