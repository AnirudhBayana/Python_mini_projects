import fitz  # PyMuPDF

def decrypt_pdf(input_path, output_path, password):
    # Open the PDF file
    pdf_document = fitz.open(input_path)

    # Check if the PDF is encrypted
    if pdf_document.isEncrypted:
        # Try to authenticate with the provided password
        if pdf_document.authenticate(password):
            # Create a new PDF writer
            pdf_writer = fitz.open()

            # Iterate over each page and copy it to the new PDF
            for page_num in range(pdf_document.page_count):
                pdf_page = pdf_document.load_page(page_num)
                pdf_writer.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

            # Save the decrypted PDF to the output file
            pdf_writer.save(output_path)
            pdf_writer.close()

            print(f"PDF decrypted successfully. Decrypted PDF saved to '{output_path}'.")
        else:
            print("Incorrect password. Unable to decrypt the PDF.")
    else:
        print("The PDF is not encrypted. No decryption needed.")

if __name__ == "__main__":
    # Set the path to the password-protected PDF
    input_path = 'D:/Programming/Python/Python_New/Naukari bill.pdf'

    # Set the path where the decrypted PDF will be saved
    output_path = 'D:/Programming/Python/Python_New/decrypted.pdf'

    # Get the password from user input
    password = "d8b8a9b7"

    # Decrypt the PDF
    decrypt_pdf(input_path, output_path, password)
