import requests

response = requests.get('http://localhost:8000/')
print(response.text)

response = requests.get('http://localhost:8000/about')
print(response.text)

data = {'username': 'admin', 'password': '123'}
response = requests.post('http://localhost:8000/login', data=data)
print(response.text)

response = requests.put('http://localhost:8000/user/1', json={'name': 'John'})
print(response.text)

response = requests.delete('http://localhost:8000/user/1')
print(response.text)
