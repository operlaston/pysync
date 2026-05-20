from pathlib import Path
import hashlib

"""
scan in all files recursively and hash them
"""
def scan_and_hash(directory):
    dir_path = Path(directory)
    file_hashes = {}

    if not dir_path.exists() or not dir_path.is_dir():
        print(f"Error: {dir_path} is not a valid directory")
        return file_hashes

    for filepath in dir_path.rglob('*'):
        if filepath.is_file():
            file_hashes[str(filepath)] = hash_file(filepath)

    return file_hashes


"""
hash a file using the md5 algorithm on its contents
"""
def hash_file(filepath):
    md5 = hashlib.md5()
    fpathbytes = bytes(filepath)
    md5.update(fpathbytes)
    return md5.hexdigest()
