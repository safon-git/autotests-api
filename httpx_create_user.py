import httpx

from httpx_get_user_me import create_user_response
from tools.fakers import get_random_email

payload = {
  "email": get_random_email(),
  "password": "rage",
  "lastName": "money",
  "firstName": "tape",
  "middleName": "na"
}

create_user_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json = payload)
create_user_response_data = create_user_response.json()
print(create_user_response_data)


