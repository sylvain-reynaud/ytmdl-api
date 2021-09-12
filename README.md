# Youtube Music Download web API

Download audio of Youtube videos using a web API

## Features

### 1.1.0

- Can download playlist by specifing `playlist=true` in `/download?url={video_url}&playlist=true`

### 1.0.0

- Download the audio of a youtube video on `/download?url={video_url}`
- The file is deleted right after the user downloads the file

## Usage

### Docker

Run image :

`docker run -p "80:80" --name youtube-dl-music-web-api youtube-dl-music-web-api:latest`

Build image :

`docker build -t youtube-dl-music-web-api .`

### Environment variables

`HOST`, default : 0.0.0.0

`PORT`, default : 80

For more, read the [FastAPI Dockerfile documentation](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker#environment-variables)

### Debugging in VS Code

You can debug the code by pressing F5 key.

## Contribute

See [CONTRIBUTE.md](./CONTRIBUTE.md)
