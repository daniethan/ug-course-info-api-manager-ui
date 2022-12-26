import asyncio
import requests, socket
from tkinter import messagebox
from decouple import config

urls = {
    'local': config('API_URL_LOCAL'),
    'online': config('API_URL_ONLINE')
}


async def is_connected(host, port=config('PORT', cast=int)):
    try:
        #try to connect to the host to check if it's reachable
        sock = socket.create_connection(address=(host, port), timeout=5)
        if sock is not None:
            # close the socket
            sock.close
        return True
    except Exception as err:
        messagebox.showerror("Connection Failed", f"Something went wrong!\n{err}")
    return False


async def get_base_uri(base_list: list[str]):
    for uri in base_list:
        is_con = await is_connected(uri)
        if is_con:
            return uri
        return urls.get('online')


class APIResources:
    BASE_URL = asyncio.run(get_base_uri(urls.values()))

    @staticmethod
    async def get_api_resource(resource: str) -> list:
        response = requests.get(url=f"{APIResources.BASE_URL}/{resource}")
        return response

    @staticmethod
    async def post_api_resource(uri: str, context: dict):
        response = requests.post(url=f"{APIResources.BASE_URL}/{uri}", json=context)
        return response.status_code
    
    @staticmethod
    async def update_api_resource(uri: str, context: dict):
        response = requests.put(url=f"{APIResources.BASE_URL}/{uri}", json=context)
        return response.status_code