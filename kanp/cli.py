from urllib.parse import quote

import click
import uvicorn

from kanp.server import app


def version():
    # wait poetry fix up: https://github.com/python-poetry/poetry/issues/1338
    # with open("pyproject.toml") as f:
    #     ret = re.findall(r'version = "(\d+\.\d+\.\d+)"', f.read())
    #     return ret[0]
    return "0.1.1"


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version(), "-V", "--version")
def cli():
    pass


@cli.command(help="Serve video server.")
@click.option("--host", default="0.0.0.0", show_default=True, help="Video server host.")
@click.option("-p", "--port", type=int, default=8000, show_default=True, help="Video server port.")
def serve(host, port: int):
    uvicorn.run(app, host=host, port=port)


@cli.command(help="Open video server url with webbrowser.")
@click.option("-s", "--server", default="http://127.0.0.1:8000", show_default=True)
@click.option("-u", "--url", required=True, help="Video url or site url support by youtube-dl.")
@click.option(
    "-y",
    "--youtube-dl",
    default=False,
    is_flag=True,
    help="Get real video url by youtube-dl.",
    show_default=True,
)
def watch(server: str, url: str, youtube_dl: bool):
    video_url = f"{server}?url={quote(url)}&ydl={1 if youtube_dl else 0}"
    print(f"Open by player or browser: {video_url}")


if __name__ == "__main__":
    cli()
