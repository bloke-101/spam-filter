from pathlib import Path

import sys
import argparse


def get_args_parsed():
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

def is_args_correct(args):
    if not args.input_dir.exists():
        print(f"{args.input_dir}: not exists!", file=sys.stderr)
        return False
    elif not args.input_dir.is_dir():
        print(f"{args.input_dir}: not a directory!", file=sys.stderr)
        return False
    elif not args.keywords.exists():
        print(f"{args.keywords}: not exists!", file=sys.stderr)
        return False
    elif not args.keywords.is_file():
        print(f"{args.input_dir}: not a file!", file=sys.stderr)
        return False
    return True

def main():
    args = get_args_parsed()
    if not is_args_correct(args):
        return

if __name__ == "__main__":
    main()
