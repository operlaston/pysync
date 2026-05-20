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
            file_hashes[str(filepath.relative_to(dir_path))] = hash_file(filepath)

    return file_hashes


"""
hash a file using the md5 algorithm on its contents
"""
def hash_file(filepath):
    md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            md5.update(chunk)
    return md5.digest()
    # return md5.hexdigest()
