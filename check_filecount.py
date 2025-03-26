#!/usr/bin/env python3
import os
import argparse

def count_directories(directory: str) -> int:
    total_directories = 0
    # os.walk yields a tuple (root, dirs, files) for each directory in the tree.
    for root, dirs, files in os.walk(directory):
        total_directories += len(dirs)
    return total_directories

if __name__ == "__main__":
    dir = "path to/WAB5_Lightrag/outputs_llama"

    if not os.path.isdir(dir):
        print(f"Error: {dir} is not a valid directory.")
        exit(1)

    total = count_directories(dir)
    print(f"Total directories under '{dir}': {total}")


