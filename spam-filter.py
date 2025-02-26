from pathlib import Path

import sys
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Filter files by keywords"
    )
    parser.add_argument(
        "input_dir",
        type=Path,
        help="An input dir for target files"
    )
    parser.add_argument(
        "keywords",
        type=Path,
        nargs="?", 
        default="./keywords.txt",
        help="An input file for keywords (default: ./keywords.txt)"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if not args.input_dir.exists():
        print(f"{args.input_dir}: not exists!", file=sys.stderr)
    elif not args.input_dir.is_dir():
        print(f"{args.input_dir}: not a directory!", file=sys.stderr)
    elif not args.keywords.exists():
        print(f"{args.keywords}: not exists!", file=sys.stderr)
    else:
        pass
