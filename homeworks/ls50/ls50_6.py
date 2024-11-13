import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {"tile": "test", "body":"Test body", "userID":1}

response = requests.post(url, data)

if response.status_code == 201:
    print("test pass", response.json())
else:
    print("fail", response.status_code)