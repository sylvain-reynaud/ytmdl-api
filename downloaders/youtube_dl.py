from __future__ import unicode_literals
import os
import youtube_dl
from enum import Enum  


title = ''


class YtDlLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def set_title_hook(d):
    global title
    if d['status'] == 'finished':
        title = d['filename']
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


async def download(url: str, shouldDownloadPlaylist: bool, download_dir: str):
    """
    Download a single music or a playlist

    Args:
        url: youtube video url
        shouldDownloadPlaylist: True to download the playlist, False if single video
        download_dir: directory where are saved the downloaded files
    """
    shouldDownloadPlaylist = False  # TODO: remove this line when the playlist download is ready
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

    return title
