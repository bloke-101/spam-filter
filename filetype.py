from enum import Enum


class FileType(str, Enum):
    TXT  = ".txt"
    DOCX = ".docx"
    PDF  = ".pdf"
