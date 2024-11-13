import requests

url = "https://jsonplaceholder.typicode.com/invalid-url"

response = requests.get(url)

response.json()

if requests.exceptions.HTTPError:
    print(f"{response.status_code}")
elif requests.exceptions.RequestException:
    print(f"error")