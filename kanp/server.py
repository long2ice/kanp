from fastapi import FastAPI
from pydantic import HttpUrl
from starlette.responses import StreamingResponse

from kanp.download import Downloader
from kanp.utils import get_real_download_url

app = FastAPI()


async def video_stream(url: str):
    async with Downloader(url) as downloader:
        async for block in downloader:
            yield block


@app.get("/")
async def get_video_stream(
    url: HttpUrl, ydl: int = 0,
):
    if ydl:
        url = get_real_download_url(url)
    return StreamingResponse(video_stream(url))
