import argparse
import scanner
import synchronizer

def main():
    parser = argparse.ArgumentParser(description="pysync")

    parser.add_argument('--source', '-s', required=True, type=str)
    parser.add_argument('--replica', '-r', required=True, type=str)
    parser.add_argument('--log-file', '-l', type=str)

    args = parser.parse_args()
    source_hashes = scanner.scan_and_hash(args.source)
    replica_hashes = scanner.scan_and_hash(args.replica)

    synchronizer.sync_dirs(source_hashes, replica_hashes, args.source, args.replica)

    # if not file_hashes:
    #     print("directory not found")
    #     return
    #
    # for file_path, hashcode in file_hashes.items():
    #     print(f"file path: {file_path}, hashcode: {hashcode}")

if __name__ == "__main__":
    main()
