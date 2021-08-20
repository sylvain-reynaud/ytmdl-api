from typing import Optional
from fastapi import FastAPI
from fastapi.responses import FileResponse
from youtube import download
import os

DOWNLOAD_DIR = os.getenv('DOWNLOAD_DIR', "./downloaded/")

app = FastAPI()


@app.get("/")
async def read_root():
    some_file_path = f"{DOWNLOAD_DIR}Kool & The Gang - Wild And Peaceful.mp3"
    # return {"Hello": "World"}
    return FileResponse(some_file_path)


@app.get("/download")
async def download_audio(url: Optional[str] = None, playlist: Optional[str] = None):
    shouldDownloadPlaylist = True if playlist else False
    # TODO : await ou non ?
    pathfile = await download(url, shouldDownloadPlaylist, DOWNLOAD_DIR)

    return FileResponse(pathfile)
    # return {"url": url, "playlist": playlist}
