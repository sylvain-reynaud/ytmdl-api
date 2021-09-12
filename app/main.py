from typing import Optional

from starlette.background import BackgroundTask
from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse
import os
from downloaders.youtube_dl import download
from files_managers.utils import slugify, delete_subdir_download

DOWNLOAD_DIR = os.getenv('DOWNLOAD_DIR', "./downloaded/")


app = FastAPI()


@app.get("/")
async def read_root():
    some_file_path = f"{DOWNLOAD_DIR}Kool & The Gang - Wild And Peaceful.mp3"
    # return {"Hello": "World"}
    return RedirectResponse("/docs#/default/download_audio_download_get")


@app.get("/download")
async def download_audio(url: Optional[str] = None, playlist: Optional[bool] = False, media_type: Optional[str] = 'webm'):
    current_download_dir = os.path.join(DOWNLOAD_DIR, slugify(url))
    pathfile = await download(url, playlist, current_download_dir)
    filename = pathfile.replace(current_download_dir, "")

    # getting the path only
    subdir_path = pathfile.replace(filename, "")
    clean_filename = filename.replace("NA -", "")

    # audio media_type info :
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#audio_and_video_types
    return FileResponse(
        path=pathfile,
        filename=clean_filename,
        media_type="audio/webm",
        background=BackgroundTask(
            delete_subdir_download, path=subdir_path, wait_minute=1)
    )
