# backend/chat/utils/file_utils.py

import hashlib

def calculate_file_hash(file):
    """
    Calculate the MD5 hash of a file.

    Parameters
    ----------
    file : File
        The file object to be hashed.

    Returns
    -------
    str
        The hexadecimal MD5 hash of the file.
    """
    hasher = hashlib.md5()
    for chunk in file.chunks():
        hasher.update(chunk)
    return hasher.hexdigest()
