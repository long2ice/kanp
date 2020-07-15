import aiofiles
import pytest

from kanp.download import Downloader


@pytest.mark.asyncio
async def test_download():
    url = 'https://dldir1.qq.com/qqfile/QQforMac/QQ_6.6.8.dmg'
    async with Downloader(url) as downloader:
        async for block in downloader:
            async with aiofiles.open('qq.dmg', 'ab+') as f:
                await f.write(block)
