# PDF Organizer

This Python script organizes scanned PDF files into folders based on user-specified keywords.

## Dependencies

- [PyMuPDF](https://pypi.org/project/PyMuPDF/): A Python binding for MuPDF, a lightweight PDF, XPS, and E-book viewer.

## Installation

1. Install the required dependencies using the following command:

    ```bash
    pip install pymupdf
    ```

## Usage

1. Clone the repository or download the script.
2. Place your scanned PDFs in a folder.
3. Run the script by executing the following command:

    ```bash
    python3 organize_pdfs.py
    ```

4. Follow the on-screen instructions to enter keywords for each PDF file.
5. The script will organize the PDFs into folders based on the specified keywords in the output directory.

## Example

Following directory structure:

/pdf-scanner
|-- organize_pdfs.py
|-- scanned_pdfs
| |-- document1.pdf
| |-- document2.pdf
|-- output

