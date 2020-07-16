import functools

import async_lru
import httpx
import youtube_dl


@functools.lru_cache()
def get_real_download_url(url: str):
    """
    get real download url by ydl
    :param url:
    :return:
    """
    params = dict(forceurl=True, format="bestvideo/best",)
    with youtube_dl.YoutubeDL(params) as ydl:
        info = ydl.extract_info(url, download=False)
        video_url = info.get("url", None)
        return video_url


@async_lru.alru_cache()
async def get_video_info(url):
    async with httpx.AsyncClient() as client:
        response = await client.head(url)
        headers = response.headers
        return int(headers.get("content-length")), headers.get("content-type")
