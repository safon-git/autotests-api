import httpx

client = httpx.Client()

response = client.get(base_url="http://localhost:8080/")

print(response.json())