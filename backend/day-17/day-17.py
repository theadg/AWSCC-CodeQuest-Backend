import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(f"GET RESPONSE {response.json()}")