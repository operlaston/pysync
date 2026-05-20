import argparse
import scanner

def main():
    parser = argparse.ArgumentParser(description="pysync")

    parser.add_argument('--source', '-s', required=True, type=str)
    parser.add_argument('--replica', '-r', required=True, type=str)
    parser.add_argument('--log-file', '-l', type=str)

    args = parser.parse_args()
    file_hashes = scanner.scan_and_hash(args.source)
    if not file_hashes:
        print("directory not found")
        return

    for file_path, hashcode in file_hashes.items():
        print(f"file path: {file_path}, hashcode: {hashcode}")

if __name__ == "__main__":
    main()
