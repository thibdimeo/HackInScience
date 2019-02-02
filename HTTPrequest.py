import requests
try:
    r = requests.get('https://api.github.com/users/python')
except:
    print("No internet connectivity.")
print(r.text)