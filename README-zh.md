# Kanp

![pypi](https://img.shields.io/pypi/v/kanp.svg?style=flat)
![docker](https://img.shields.io/docker/cloud/build/long2ice/kanp)
![license](https://img.shields.io/github/license/long2ice/kanp)
![workflows](https://github.com/long2ice/kanp/workflows/pypi/badge.svg)
![workflows](https://github.com/long2ice/kanp/workflows/ci/badge.svg)

[English](https://github.com/long2ice/kanp/blob/dev/README.md)

## 简介

使用多线程边下边看。

## 安装

```shell
> pip install kanp
```

## 使用

```shell script
Usage: kanp [OPTIONS] COMMAND [ARGS]...

Options:
  -V, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  serve  Serve video server.
  watch  Open video server url with webbrowser.
```

### 启动服务器

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

或使用 docker 启动：

```shell script
> docker run -d -p 8000:8000 long2ice/kanp
```

你将会看到：

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

### 使用浏览器观看

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

将会打开浏览器自动播放。

享受流畅的观看体验吧！

## License

本项目遵从 [Apache-2.0](https://github.com/long2ice/kanp/blob/master/LICENSE) 开源许可。
