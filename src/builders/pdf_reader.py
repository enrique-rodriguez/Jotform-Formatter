import pdfplumber


with pdfplumber.open(pdf) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()