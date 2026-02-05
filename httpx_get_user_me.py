import httpx

body_create_user = {
  "email": "dota2@example.com",
  "password": "rage",
  "lastName": "money",
  "firstName": "tape",
  "middleName": "na"
}

create_user_response = httpx.post('http://localhost:8000/api/v1/users', json=body_create_user)
create_user_response_json = create_user_response.json()
print('Создание аккаунта')
print(create_user_response_json)

body_login_request = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=body_login_request)
print('Вход в аккаунт')
print(login_response.status_code)
print(login_response.json())