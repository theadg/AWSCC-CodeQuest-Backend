import requests

# Example GET request to fetch user data
response = requests.get("https://api.example.com/users/123")
print("GET Response:", response.text)

# Example POST request to create a new user
new_user_data = {"username": "new_user", "email": "new@example.com"}
response = requests.post("https://api.example.com/users", json=new_user_data)
print("POST Response:", response.text)

# Example PUT request to update user information
updated_data = {"email": "updated@example.com"}
response = requests.put("https://api.example.com/users/123", json=updated_data)
print("PUT Response:", response.text)

# Example DELETE request to remove a user
response = requests.delete("https://api.example.com/users/123")
print("DELETE Response:", response.text)