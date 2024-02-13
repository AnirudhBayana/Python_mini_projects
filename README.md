PDF Decryption Tool
This Python script decrypts a password-protected PDF file using the PyMuPDF library.

Prerequisites
Python 3.x
PyMuPDF library
You can install the required library using pip:

bash
Copy code
pip install PyMuPDF
Usage
Clone this repository or download the decrypt_pdf.py file.

Navigate to the directory containing decrypt_pdf.py in your terminal.

Run the script by executing the following command:

bash
Copy code
python decrypt_pdf.py
You will be prompted to provide the following information:

Path to the input password-protected PDF file.
Path where the decrypted PDF will be saved.
Password for decrypting the PDF.
Once provided, the script will attempt to decrypt the PDF using the provided password. If the password is correct, it will save the decrypted PDF to the specified output path.

Notes
If the provided password is incorrect, the script will display an error message indicating that decryption failed due to an incorrect password.

If the PDF is not encrypted, the script will indicate that no decryption is needed.

Ensure that you have the necessary permissions to decrypt the PDF file.

Please remember to handle sensitive information securely, especially passwords.
