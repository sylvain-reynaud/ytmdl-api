from typing import Optional
from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse
from youtube.download import download
import os

DOWNLOAD_DIR = os.getenv('DOWNLOAD_DIR', "./downloaded/")

app = FastAPI()


@app.get("/")
async def read_root():
    some_file_path = f"{DOWNLOAD_DIR}Kool & The Gang - Wild And Peaceful.mp3"
    # return {"Hello": "World"}
    return RedirectResponse("/docs#/default/download_audio_download_get")


@app.get("/download")
async def download_audio(url: Optional[str] = None, playlist: Optional[bool] = False):
    pathfile = await download(url, playlist, DOWNLOAD_DIR)
    filename = pathfile.replace(DOWNLOAD_DIR, "").replace("NA -", "")
    # audio media_type info :
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#audio_and_video_types
    return FileResponse(path=pathfile, filename=filename, media_type="audio/webm")
