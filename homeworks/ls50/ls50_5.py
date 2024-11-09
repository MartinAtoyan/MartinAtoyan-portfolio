
import requests

url = "https://jsonplaceholder.typicode.com/posts"
parameter = {"userID" : 1}

response = requests.get(url, parameter)

if response.status_code == 200:
    posts = response.json()

    for post in posts:
        print(post['title'])

else:
    print(response.status_code)