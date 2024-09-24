from aiohttp import ClientSession


class HTTPClient:
    def __init__(self, base_url):
        self._session = ClientSession(
            base_url=base_url,
            headers={

            },
        )


class GetDataPeek(HTTPClient):
    async def get_data(self):
        async with self._session.get('http://10.179.107.129/') as resp:
            result = await resp.json()
            print(f'result: {result}')
            return result

