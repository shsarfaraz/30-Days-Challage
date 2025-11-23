import io
import PyPDF2

def extract_text_from_pdf(pdf_bytes: bytes) -> str | None:
    """
    Extracts text from the bytes of a PDF file.

    Args:
        pdf_bytes: The content of the PDF file as bytes.

    Returns:
        A string containing the extracted text, or None if an error occurs.
    """
    try:
        pdf_file = io.BytesIO(pdf_bytes)
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
