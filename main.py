import argparse
from dataclasses import dataclass
from datetime import datetime
import os

from library import (
    PDFExtractorBase,
    PDFMinerExtractor,
    PFPlumberExtractor,
    PyMuExtractor,
    PyPDFExtractor,
)

pypdf = PyPDFExtractor()
pymy = PyMuExtractor()
pdfminer = PDFMinerExtractor()
pfplumber = PFPlumberExtractor()


extractors = {
    pypdf.name: pypdf,
    pymy.name: pymy,
    pdfminer.name: pdfminer,
    pfplumber.name: pfplumber,
}


@dataclass
class Result:
    extractor_id: str
    elapsed_time: int


def evaluate_time(directory: str, extractor: PDFExtractorBase) -> Result:
    start_time = datetime.now()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        extractor.load(file_path)
    elapsed_time = datetime.now() - start_time

    return Result(elapsed_time=elapsed_time.seconds, extractor_id=extractor.name)


def append_text_to_file(file_path, text):
    with open(file_path, "a") as file:
        file.write(text)


def evaluate_content(directory: str, result: str, extractor: PDFExtractorBase) -> None:
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        pdf = extractor.load(file_path)

        suffix = extractor.name.lower()
        text_filename = filename.replace(".pdf", f"_{suffix}.txt")
        result_path = os.path.join(result, text_filename)

        for page in pdf.pages:
            append_text_to_file(result_path, page.content)

        print(result_path)


def main(args):
    print(f"{args.directory=}")

    for _, extractor in extractors.items():
        # time_result = evaluate_time(args.directory, extractor)
        # print(time_result)
        evaluate_content(args.directory, args.result, extractor)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        help="Path to directory containing the PDF files",
        required=True,
    )

    parser.add_argument(
        "-r",
        "--result",
        type=str,
        help="Path to directory to save the extracted text",
        required=True,
    )

    main(parser.parse_args())
