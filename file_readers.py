from docx import Document
from pdfminer.high_level import extract_text


def read_txt(filepath):
    with open(filepath) as f:
        return f.read()

def read_docx(filepath):
    paragraphs = Document(filepath).paragraphs
    doc_text = [p.text for p in paragraphs]
    tables = []
    for table in tables:
        for row in table.rows:
            for cell in row.cells:
                tables.append(cell.text)
    doc_text.extend(tables)
    return " ".join(doc_text)

def read_pdf(filepath):
    with open(filepath, "rb") as f:
        return extract_text(f)
