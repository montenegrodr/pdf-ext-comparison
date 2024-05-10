# pdf-ext-comparison

Comparison of PDF's text extraction tools

- [PyPDF](https://pypi.org/project/pypdf/)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
- [PDFMiner](https://pypi.org/project/pdfminer/)
- [PDFPlumber](https://github.com/jsvine/pdfplumber)

Usage:

1. Drop your files to a directory `$(FILES_DIRECTORY_PATH)`.
2. Run `python3 main.py -d $(FILES_DIRECTORY_PATH) -r $(RESULTS_DIRECTOY_PATH)`

## Results

The elapsed time when extracting the textual content from all available PDFs.

![](/imgs/time_hist.png)

Manual quality assessment of the results.

**PDFMiner**:

Keeps most of the original format and itemizations and I could not find a single extraction error.
But it sometimes, adds some unnecessary spaces between pages

**PDFPlumber**:

It does a crappy job of keeping the original structure of the document.

**PyMUPDF**:

Keeps most of the original document structure with some errors

**PYPDF**:

Comparable with PDFMiner with structured texts but it does not work well with presentations.