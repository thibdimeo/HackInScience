import requests
req = requests.get("http://127.0.0.1:8080/byebye")
print(req.status_code)
print(req.content)


