from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


@dataclass
class PDFPage:
    content: str


@dataclass
class PDFFile:
    pages: List[PDFPage] = field(default_factory=list)

    def add_page(self, page: PDFPage):
        self.pages.append(page)


class PDFExtractorBase(ABC):

    @abstractmethod
    def load(self, file_path: str) -> PDFFile:
        pass


class PyPDFExtractor(PDFExtractorBase):
    """
    PDF extractor for https://pypi.org/project/pypdf/
    """

    def __init__(self) -> None:
        self.name = "PyPDF"

    def load(self, file_path: str) -> PDFFile:
        from pypdf import PdfReader

        pdf = PDFFile()

        reader = PdfReader(file_path)
        for page in reader.pages:
            text = page.extract_text()
            pdf.add_page(PDFPage(content=text))

        return pdf


class PyMuExtractor(PDFExtractorBase):
    """
    PDF extractor for PyMu
    """

    def __init__(self) -> None:
        self.name = "PyMuPDF"

    def load(self, file_path: str) -> PDFFile:
        import fitz

        pdf = PDFFile()

        document = fitz.open(file_path)
        for page in document:
            text = page.get_text()
            pdf.add_page(PDFPage(content=text))

        document.close()

        return pdf


class PDFMinerExtractor(PDFExtractorBase):
    """
    PDF extractor for PDFMiner.six
    """

    def __init__(self) -> None:
        self.name = "PDFMiner"

    def load(self, file_path: str) -> PDFFile:
        from pdfminer.high_level import extract_text

        pdf = PDFFile()
        text = extract_text(file_path)
        pdf.add_page(PDFPage(content=text))

        return pdf


class PFPlumberExtractor(PDFExtractorBase):
    """
    PDF extractor for PDFPlumber
    """

    def __init__(self) -> None:
        self.name = "PDFPlumber"

    def load(self, file_path: str) -> PDFFile:
        import pdfplumber

        pdf = PDFFile()

        with pdfplumber.open(file_path) as pdf_file:
            for page in pdf_file.pages:
                text = page.extract_text()
                pdf.add_page(PDFPage(content=text))

        return pdf

