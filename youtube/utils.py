from unicodedata import normalize
from re import sub
from shutil import rmtree


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = normalize('NFKC', value)
    else:
        value = normalize('NFKD', value).encode(
            'ascii', 'ignore').decode('ascii')
    value = sub(r'[^\w\s-]', '', value.lower())
    return sub(r'[-\s]+', '-', value).strip('-_')


def delete_subdir_download(path: str, wait_minute: int):
    """
    Delete a subdirectory where files are downloaded.

    Args:
        path (str): Path to the subdirectory where files are downloaded
    """
    rmtree(path)
