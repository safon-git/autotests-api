from os import access

import httpx

# данные для регистрации
data = {"email": "kir2@example.com",
  "password": "123",
  "lastName": "nam",
  "firstName": "kir",
  "middleName": "vld"}

#регистрируем пользователя
r = httpx.post("http://localhost:8000/api/v1/users", json=data)
print(r.json())

# авторизация
data = {"email": "kir2@example.com",
        "password": "123"}
r = httpx.post("http://localhost:8000/api/v1/authentication/login", json=data)
response_data = r.json()
print(response_data)

#запоминаем access_token
access_token = response_data['token']['accessToken']
print(access_token)

#запрашиваем данные пользователя
headers = {"Authorization": f"Bearer {access_token}"}
r = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(r.json())





