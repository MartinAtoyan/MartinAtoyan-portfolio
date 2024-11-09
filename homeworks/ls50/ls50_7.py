import requests

url = "https://jsonplaceholder.typicode.com/invalid-url"

try:
    response = requests.get(url)

    response.raise_for_status()
    print("Request succeeded:", response.json())

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err} - Status code: {response.status_code}")
except requests.exceptions.RequestException as req_err:
    print(f"Error occurred: {req_err}")
