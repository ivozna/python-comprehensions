import sys
from typing import List


def read_file_names(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        file_names = f.read().split(",")
        return file_names


def read_files_and_combine(file_names: List[str]) -> List[str]:
    texts = []
    for file in file_names:
        with open(file, "r") as f:
            texts.append(f.read())
    return texts


def write_result(file_name: str, texts: List[str]) -> None:
    with open(file_name, "w") as f:
        f.write("\n".join(texts))


def main() -> None:
    list_of_files = read_file_names(sys.argv[1])
    texts = read_files_and_combine(list_of_files)
    print(f"Combined {len(texts)} files.\nResult saved to {sys.argv[2]}.")
    write_result(sys.argv[2], texts)


if __name__ == ("__main__"):
    main()
