import httpx

# HTTP вообще крутой

# Может делать get запросы--------------
response = httpx.get('http://jsonplaceholder.typicode.com/todos/1')

print(response.status_code)
print(response.json())

# Передавать json данные----------
data = {
    "title": 'Блотняк перекосяк',
    "completed": False,
    "userId": 1
}

response = httpx.post('http://jsonplaceholder.typicode.com/todos', json=data)

print(response.status_code)
print(response.request.headers)
print(response.json())

# И другие данные в теле-----------
data = {"username": "djtape", "password": "22905"}
response = httpx.post('https://httpbin.org/post', data=data)

print(response.status_code)
print(response.request.headers)
print(response.json())

# Как и заголовки------------
headers = {"Authorization": "Bearer"}
httpx.get('https://httpbin.org/get', headers=headers)

print(response.request.headers)
print(response.json())

# Так и Query параметры-----------
params = {"userId": 1}
response = httpx.get('http://jsonplaceholder.typicode.com/todos', params=params)

print(response.url)
print(response.json())

# -------------------Отправлять файлы------------
#files = {'file': {"example.txt", open("example.txt", "rb")}}
#response = httpx.post('https://httpbin.org/post', files=files)
#print(response.json())

# использовать api клиенты
with httpx.Client() as client:
    response1 = client.get('http://jsonplaceholder.typicode.com/todos/1')
    response2 = client.get('http://jsonplaceholder.typicode.com/todos/2')

print(response1.json())
print(response2.json())

# передавать одни и те же заголовки
client = httpx.Client(headers={"Authorization": "Bearer"})
response = client.get('https://httpbin.org/get')

print(response.json())

# работать с ошибками

try:
    response = httpx.get('http://jsonplaceholder.typicode.com/invalid-url')
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'Ошибка запроса: {e}')

# работа с таймаутом
try:
    response = httpx.get('http://jsonplaceholder.typicode.com/details/1', timeout=2)
except httpx.ReadTimeout as e:
    print("Слишком долго тайм-аут")