from kanp.utils import get_real_download_url


def test_get_real_download_url():
    url = "https://www.youtube.com/watch?v=WLVuUTUbhkw"
    get_real_download_url(url)
