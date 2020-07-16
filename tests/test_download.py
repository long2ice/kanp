import hashlib

import aiofiles
import pytest
from aiofiles import os

from kanp.download import Downloader


@pytest.mark.asyncio
async def test_download():
    url = "https://raw.githubusercontent.com/long2ice/kanp/dev/.dockerignore"
    file = ".dockerignore.txt"
    async with aiofiles.open(file, "ab+") as f:
        async with Downloader(url) as downloader:
            async for block in downloader:
                await f.write(block)

    async with aiofiles.open(file, "rb") as f:
        assert hashlib.md5(await f.read()).hexdigest() == "c59066fc1c16d900c6c9275c5f4a1757"
    await os.remove(file)
