import requests

endpoint = 'https://jsonplaceholder.typicode.com/posts'

headers = {
    'User-Agent': 'MyApp/1.0'
}

response = requests.get(endpoint, headers=headers)
print(f"Status Code: {response.status_code}")
print(f"Response Headers: {response.headers}")
print(f"Response Content: {response.text}")

newPost = {
    'title': 'Sample Title',
    'body': 'Sample Body'
}

postResponse = requests.post(endpoint, json=newPost)
print(f"Status Code: {postResponse.status_code}")
print(f"Response Content: {postResponse.text}")
