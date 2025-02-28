from docx import Document
from pdfminer.high_level import extract_text


def read_txt(filepath):
    with open(filepath) as f:
        return f.read()

def read_docx(filepath):
    document = Document(filepath)
    doc_text = [p.text for p in document.paragraphs]
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                doc_text.append(cell.text)
    return " ".join(doc_text)

def read_pdf(filepath):
    with open(filepath, "rb") as f:
        return extract_text(f)
