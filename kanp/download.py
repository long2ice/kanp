import asyncio
import io

import httpx


class Downloader:
    client = httpx.AsyncClient(trust_env=True)
    range_size = 1024 * 1024 * 5

    def __init__(self, url: str):
        self.url = url
        self.blocks = asyncio.Queue(maxsize=10)
        self.semaphore = asyncio.Semaphore(5)

    async def __aenter__(self):
        self.downloader = asyncio.ensure_future(self.download())
        return self

    async def __aexit__(self, type, value, tb):
        self.downloader.cancel()
        while not self.blocks.empty():
            self.blocks.get_nowait()
        await self.downloader

    async def __aiter__(self):
        while not (self.downloader.done() and self.blocks.empty()):
            chunk = await self.blocks.get()
            yield chunk

    async def _download_range(self, i, req_headers):
        async with self.semaphore:
            async with self.client.stream('GET', self.url, headers=req_headers) as resp:
                buffer = io.BytesIO()
                async for chunk in resp.aiter_bytes():
                    buffer.write(chunk)
                await self.blocks.put(buffer.getvalue())

    async def download(self):
        async with self.client.stream('GET', self.url, ) as response:
            headers = response.headers
            content_length = int(headers.get('content-length'))
        last_range = 0
        tasks = []
        for i in range(0, content_length, self.range_size):
            if i > 0:
                req_headers = {
                    'Range': f"bytes={last_range}-{i}"
                }
                last_range = i + 1
                tasks.append(self._download_range(i, req_headers))
        await asyncio.gather(*tasks)
