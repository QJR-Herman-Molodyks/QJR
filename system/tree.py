
import os

def tree(path: str, prefix: str = "", dirs: int = 0, files: int = 0):
    entries = sorted(os.listdir(path))

    for index, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last = index == len(entries) - 1
        branch = "└── " if is_last else "├── "

        print(f"{prefix}{branch}{entry}")

        files += len(os.listdir(path))

        if os.path.isdir(full_path):
            dirs += 1
            next_prefix = prefix + ("    " if is_last else "│   ")
            tree(full_path, next_prefix, dirs, files)

if __name__ == "__main__":
    print(".")
    tree(".")
