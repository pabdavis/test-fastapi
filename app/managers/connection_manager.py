from typing import Dict
from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, client_id: int):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id: int):
        del self.active_connections[client_id]

    async def send_message(self, client_id: int, message: str):
        websocket = self.active_connections[client_id]
        await websocket.send_text(message)

    # async def broadcast(self, message: str):
    #     for connection in self.active_connections:
    #         await connection.send_text(message)