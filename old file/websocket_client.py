import asyncio
from http.client import responses

import websockets

async def client():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        message = "Привет сервер!"
        print(f'Отправлка: {message}')
        await websocket.send(message)

        response = await websocket.recv()
        print(f'ответ от сервера: {response}')

asyncio.run(client())