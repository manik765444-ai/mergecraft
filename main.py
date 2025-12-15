# main.py

import os
from PyPDF2 import PdfMerger, PdfReadError


def merge_pdfs(output_path, *input_files):
    """
    Merges multiple PDF files into a single PDF.

    Args:
        output_path (str): The path where the merged PDF will be saved.
        *input_files (str): Paths to the PDF files to be merged.

    Raises:
        FileNotFoundError: If one of the input files does not exist.
        ValueError: If no input files are provided.
        PdfReadError: If there is an issue reading the input files.
    """
    if not input_files:
        raise ValueError("No input files provided for merging.")

    merger = PdfMerger()

    try:
        for pdf_file in input_files:
            if not os.path.exists(pdf_file):
                raise FileNotFoundError(f"File not found: {pdf_file}")
            merger.append(pdf_file)
        
        merger.write(output_path)
        print(f"PDFs merged successfully into: {output_path}")
    except PdfReadError as e:
        print(f"Error while reading PDF files: {e}")
        raise
    except FileNotFoundError as fnfe:
        print(f"File error: {fnfe}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
    finally:
        merger.close()


def main():
    """
    The main function to execute the script.
    """
    # List of PDF files to be merged (example)
    pdf_files = [
        "file1.pdf",
        "file2.pdf",
        "file3.pdf"
    ]
    
    # Define the output file name
    output_pdf = "merged_output.pdf"

    try:
        merge_pdfs(output_pdf, *pdf_files)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError: {fnfe}")
    except PdfReadError as pre:
        print(f"PdfReadError: {pre}")
    except Exception as e:
        print(f"An unexpected error occurred in the main function: {e}")


if __name__ == "__main__":
    main()