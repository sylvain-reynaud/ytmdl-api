from __future__ import unicode_literals
import os
from typing import Optional
import youtube_dl
from enum import Enum
import zipfile


filename = ''


class YtDlLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def set_title_hook(d):
    global filename
    if d['status'] == 'finished':
        filename = d['filename']
        # print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    # 'postprocessors': [{
    #     'key': 'FFmpegExtractAudio',
    #     'preferredcodec': 'mp3',
    #     'preferredquality': '256',
    # }],
    'logger': YtDlLogger(),
    'progress_hooks': [set_title_hook],
    'forcefilename': True
}

async def download(url: str, download_dir: str, shouldDownloadPlaylist: Optional[bool] = False):
    """
    Download a single music or a playlist

    Args:
        url: youtube video url
        shouldDownloadPlaylist: True to download the playlist, False if single video
        download_dir: directory where are saved the downloaded files
    """
    print('video url :', url)
    print('download playlist ? :', shouldDownloadPlaylist)

    # setting youtube_dl options
    opts = ydl_opts
    opts['noplaylist'] = not(shouldDownloadPlaylist)
    opts['outtmpl'] = os.path.join(
        download_dir, '%(creator)s - %(title)s.%(ext)s')

    # download
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
# if shouldDownloadPlaylist, then make a zip file with all the files
    if shouldDownloadPlaylist:
        filename = zip_playlist(download_dir)

    return filename


def zip_playlist(download_dir):
    print('making zip file ...')
    zip_filename = 'playlist.zip'
    zip_pathfile = os.path.join(download_dir, zip_filename)
    zip_file = zipfile.ZipFile(zip_pathfile, 'w')
    files = os.listdir(download_dir)
    print(files)
    print(zip_pathfile)
    files.remove(zip_filename)  # avoid infinite loop
    print(files)
    for file in files:
        zip_file.write(os.path.join(download_dir, file), file)
    zip_file.close()
    print('zip file', zip_pathfile, 'created')
    filename = zip_pathfile
    return filename
