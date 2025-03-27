# Spam-Filter

**The Spam-Filter** is a CLI tool to filter files by keywords. If a file is
marked as spam, the tool moves the file to the directory named as
**./spam**.

The Spam-Filter is based on **the Aho–Corasick algorithm**. It is a
kind of dictionary-matching algorithm that locates elements of a finite
set of strings within an input text. It matches all strings
simultaneously.

If amount of matched strings is **10% or more** of the input text, the
file with the input text is marked as spam.

## Supported file types

- TXT
- DOCX
- PDF

The tool decides if a file type is supported or not by its extension.

## How to deploy the tool

``python -m venv .venv``

``source .venv/bin/activate``

``pip install -r requirements.txt``

## How to run the tool

``python spam_filter.py input_dir keyword_file``

``input_dir`` - a directory containing files to scan;

``keyword_file`` - a file containing keywords.

``python spam_filter.py -h`` to get more help information.
