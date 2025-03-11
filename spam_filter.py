from pathlib import Path

from trie import Trie
from filetype import FileType
from file_readers import read_txt
from file_readers import read_pdf
from file_readers import read_docx

import os
import sys
import shutil
import argparse

MAX_SPAM_LEVEL = 0.1
SPAM_DIR = "./spam"
KEYWORD_DIR = "./keywords.txt" 


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
        default=KEYWORD_DIR,
        help=f"An input file for keywords (default: {KEYWORD_DIR})"
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

def fill_in(trie, keyword_path):
    with open(keyword_path, "r", encoding="UTF-8") as f:
        for keyword in f:
            trie.insert(keyword.strip().lower())

def create_trie(keywords):
    trie = Trie()
    fill_in(trie, keywords)
    trie.set_suf_links()
    return trie

def make_spam_dir():
    spam_dir = Path(SPAM_DIR)
    if not spam_dir.exists():
        os.makedirs(spam_dir)
    return spam_dir            

def is_supported_filetype(filepath):
    if filepath.suffix == FileType.TXT:
        return True
    elif filepath.suffix == FileType.DOCX:
        return True
    elif filepath.suffix == FileType.PDF:
        return True
    return False

def get_text(filepath):
    if filepath.suffix == FileType.TXT:
        return read_txt(filepath).lower().strip()
    elif filepath.suffix == FileType.DOCX:
        return read_docx(filepath).lower().strip()
    elif filepath.suffix == FileType.PDF:
        return read_pdf(filepath).lower().strip()
    else:
        return None

def get_word_count(filepath):
    count = 0
    with open(filepath, "r") as f:
        for line in f:
            count += len(line.strip().split())
    return count

def show_spam_files(spam_files):
    if not spam_files:
        print("There is no spam!")
        return
    print("The following files has been marked as spam:")
    for i, f in enumerate(spam_files, 1):
        print(f"{i}. {f}")

def main():
    args = get_args_parsed()
    if not is_args_correct(args):
        return 
    
    trie = create_trie(args.keywords)
    spam_dir = make_spam_dir()    

    spam_files = []
    for filename in os.listdir(args.input_dir):
        filepath = args.input_dir / Path(filename)
        if not is_supported_filetype(filepath):
            continue
        if (word_count := get_word_count(filepath)) == 0:
            continue
        text = get_text(filepath)
        pattern_count = trie.get_pattern_count(text)
        if pattern_count / word_count >= MAX_SPAM_LEVEL:
            shutil.move(filepath, spam_dir)
            spam_files.append(filepath)
    show_spam_files(spam_files)

if __name__ == "__main__":
    main()
