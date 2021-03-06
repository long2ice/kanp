from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse

from kanp.download import Downloader
from kanp.utils import get_real_download_url, get_video_info

app = FastAPI()


async def video_stream(url: str, range_: int, content_length: int):
    async with Downloader(url, range_, content_length) as downloader:
        async for block in downloader:
            yield block


@app.route("/", methods=["GET", "HEAD"])
async def get_video_stream(request: Request):
    range_ = request.headers.get("Range")
    ydl = request.query_params.get("ydl") or 0
    url = request.query_params.get("url")
    if ydl:
        url = get_real_download_url(url)
    content_length, content_type = await get_video_info(url)
    if not range_:
        start_range = 0
        status_code = 200
        headers = {
            "Content-Length": str(content_length),
            "Content-Type": content_type,
            "Accept-Ranges": "bytes",
        }
    else:
        start_range = int(range_[6:].split("-")[0])
        status_code = 206
        headers = {
            "Content-Type": content_type,
            "Content-Range": f"bytes {start_range}-{content_length - 1}/{content_length}",
        }
    if request.method == "GET":
        return StreamingResponse(
            status_code=status_code,
            content=video_stream(url, start_range, content_length),
            headers=headers,
        )
    elif request.method == "HEAD":
        return Response(status_code=status_code, headers=headers,)
