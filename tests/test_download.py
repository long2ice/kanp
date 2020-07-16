import hashlib

import aiofiles
import pytest
from aiofiles import os

from kanp.download import Downloader


@pytest.mark.asyncio
async def test_download():
    url = "https://dldir1.qq.com/qqfile/QQforMac/QQ_6.6.8.dmg"
    file = "qq.dmg"
    # url = 'https://r4---sn-q4fl6n7e.googlevideo.com/videoplayback?expire=1594893288&ei=iM8PX6uBEs2ulQTipb-IDw&ip=2001%3A19f0%3A7001%3A3b68%3A5400%3A2ff%3Afed8%3Aa942&id=o-AE7YKFRGO-BVua5vqBvsajPUtN7YeDd5_ZkcV3q0QmGN&itag=303&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C298%2C299%2C302%2C303&source=youtube&requiressl=yes&mh=e4&mm=31%2C29&mn=sn-q4fl6n7e%2Csn-q4flrn7s&ms=au%2Crdu&mv=m&mvi=4&pl=51&initcwndbps=2763750&vprv=1&mime=video%2Fwebm&gir=yes&clen=203607118&dur=838.587&lmt=1594746667948482&mt=1594871606&fvip=4&keepalive=yes&fexp=23883097&beids=9466588&c=WEB&txp=5535432&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgE-ZuBliJpodoJnG5hxORx_HZ5GxBX-A71OvO985KFMkCIDB3oYpxA_P1z2fxoGfhs9LT0ToLrL_54ktlL-6P5PtQ&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAMWM4kehZv4qQUecqa2GAH1RmFVep8GT8OIILEBFmllkAiBj2KCcDMDeHKleCkgPlQ1NJRD2F48YOqV_DBGEFGXm3g%3D%3D&ratebypass=yes'
    async with aiofiles.open(file, "ab+") as f:
        async with Downloader(url) as downloader:
            async for block in downloader:
                await f.write(block)

    async with aiofiles.open(file, "rb") as f:
        assert hashlib.md5(await f.read()).hexdigest() == "cb25d055edab856b643ac36482ba3f53"
    await os.remove(file)
