import httpx

from httpx_example import response

payload = {
  "email": "flex@example.com",
  "password": "1234",
  "lastName": "PUMP",
  "firstName": "LIL",
  "middleName": "esketit"
}

response = httpx.post('http://localhost:8000/api/v1/users', data=payload)
print(response.json())

response = httpx.get('http://localhost:8000/api/v1/users/me')
print(response.json())