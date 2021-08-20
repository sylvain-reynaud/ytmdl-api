from __future__ import unicode_literals
import time
import youtube_dl

title = "no title"


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
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
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'outtmpl': '%(creator)s - %(title)s.%(ext)s',
    'forcefilename': True
}


def download(url, shouldDownloadPlaylist, download_dir):
    print('video url :', url)
    print('download playlist ? :', shouldDownloadPlaylist)

    opts = ydl_opts
    opts['noplaylist'] = not(shouldDownloadPlaylist)
    opts['outtmpl'] = download_dir + opts['outtmpl']

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # filename = title.replace(download_dir, '')
    # print('Filename :', filename)
    return title
