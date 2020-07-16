import youtube_dl


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
