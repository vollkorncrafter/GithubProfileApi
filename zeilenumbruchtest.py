import requests
response = requests.get("https://api.github.com/users/moozii")
response = response.json()
print(response)