from pypdf import PdfReader

pdf_path = r"C:\Users\gouri\OneDrive\Documents\GOURI NANDHAN P V - RESUME (2026).pdf"

try:
    reader = PdfReader(pdf_path)

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        print(f"\n--- Page {page_number} ---")
        print(text if text else "No extractable text found.")

except FileNotFoundError:
    print("PDF file not found.")
except Exception as error:
    print(f"Error reading PDF: {error}")