import shutil
from pathlib import Path
import os

# source_files is the dictionary of paths to hashes for source dir
# replica_files is the dictionary of paths to hashes for replica dir
def sync_dirs(source_file_hashes, replica_file_hashes, source_dir_path,
              replica_dir_path):
    source_set = set()
    replica_set = set()

    for filepath in source_file_hashes:
        source_set.add(filepath)
    for filepath in replica_file_hashes:
        replica_set.add(filepath)

    create_set = source_set - replica_set
    remove_set = replica_set - source_set

    intersection = source_set & replica_set
    update_set = set()
    for filepath in intersection:
        if source_file_hashes[filepath] != replica_file_hashes[filepath]:
            update_set.add(filepath)
    
    for filepath in create_set:
        source_file_path = Path(source_dir_path + '/' + filepath)
        replica_file_path = Path(replica_dir_path + '/' + filepath)

        # create directories that might not yet exist
        replica_file_path.parent.mkdir(parents=True, exist_ok=True)

        shutil.copy2(source_file_path, replica_file_path) 
        print(f"created {replica_file_path}")

    for filepath in update_set:
        source_file_path = source_dir_path + '/' + filepath
        replica_file_path = replica_dir_path + '/' + filepath

        shutil.copy2(source_file_path, replica_file_path) 
        print(f"updated {replica_file_path}")

    for filepath in remove_set:
        os.remove(replica_dir_path + '/' + filepath) 
        print(f"removed {replica_dir_path + '/' + filepath}")
