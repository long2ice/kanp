# Kanp

![pypi](https://img.shields.io/pypi/v/kanp.svg?style=flat)
![docker](https://img.shields.io/docker/cloud/build/long2ice/kanp)
![license](https://img.shields.io/github/license/long2ice/kanp)
![workflows](https://github.com/long2ice/kanp/workflows/pypi/badge.svg)
![workflows](https://github.com/long2ice/kanp/workflows/ci/badge.svg)

[中文文档](https://github.com/long2ice/kanp/blob/dev/README-zh.md)

## Introduction

See video with downloading by multithread.

## Install

```shell
> pip install kanp
```

## Usage

```shell script
Usage: kanp [OPTIONS] COMMAND [ARGS]...

Options:
  -V, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  serve  Serve video server.
  watch  Open video server url with webbrowser.
```

### Serve video server

```shell script
Usage: kanp serve [OPTIONS]

  Serve video server.

Options:
  --host TEXT         Video server host.  [default: 0.0.0.0]
  -p, --port INTEGER  Video server port.  [default: 8000]
  -h, --help          Show this message and exit.

```

```shell script
> kanp serve
```

Or run with docker:

```shell script
> docker run -d -p 8000:8000 long2ice/kanp
```

And you will see:

```log
INFO:     Started server process [41254]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
CINFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [41254]
```

### Watch video by web browser

```shell script
Usage: kanp watch [OPTIONS]

  Open video server url with webbrowser.

Options:
  -s, --server TEXT  [default: http://127.0.0.1:8000]
  -u, --url TEXT     Video url or site url support by youtube-dl.  [required]
  -y, --youtube-dl   Get real video url by youtube-dl.  [default: False]
  -h, --help         Show this message and exit.
```

```shell script
> kanp watch -u 'https://www.youtube.com/watch?v=WLVuUTUbhkw' -y
```

Will open browser automatically and play video.

Just enjoy it with huge speed!

## License

This project is licensed under the [Apache-2.0](https://github.com/long2ice/kanp/blob/master/LICENSE) License.
