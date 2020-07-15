import asyncio
import io

import httpx


class Downloader:
    client = httpx.AsyncClient(trust_env=True)
    range_size = 1024 * 1024
    block_size = range_size * 5

    def __init__(self, url: str):
        self.url = url
        self.blocks = asyncio.Queue()

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

    async def _download_range(self, start_range: int, end_range: int):
        headers = {
            'Range': f"bytes={start_range}-{end_range}"
        }
        print(headers)
        buffer = io.BytesIO()
        async with self.client.stream('GET', self.url, headers=headers) as resp:
            async for chunk in resp.aiter_bytes():
                buffer.write(chunk)
        return buffer

    async def _download_block(self, start_range: int, end_range: int):
        last_range = start_range
        tasks = []
        for i in range(start_range, end_range, self.range_size):
            if 0 < i != last_range:
                tasks.append(self._download_range(last_range, i))
                last_range = i + 1
        tasks.append(self._download_range(last_range, end_range))
        buffers = await asyncio.gather(*tasks)
        for buffer in buffers:
            await self.blocks.put(buffer.getvalue())

    async def download(self):
        async with self.client.stream('GET', self.url, ) as response:
            headers = response.headers
            content_length = int(headers.get('content-length'))
        last_range = 0
        tasks = []
        for i in range(0, content_length, self.block_size):
            if 0 < i != last_range:
                tasks.append(self._download_block(last_range, i))
                last_range = i + 1
        tasks.append(self._download_block(last_range, content_length))
        await asyncio.gather(*tasks)
