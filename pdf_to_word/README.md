# PDF to Word Converter

This Python script converts PDF files into Word documents (.docx) using the `pdf2docx` library.

## Installation

1. Clone this repository:
   ```
   git clone <repository_url>
   ```

2. Install the required dependencies:
   ```
   pip install pdf2docx
   ```

## Usage

1. Place your PDF file in a directory accessible to the script.

2. Update the `pdf_file_path` variable in the script with the path to your PDF file.

3. Update the `word_file_path` variable with the desired path where the Word document will be saved.

4. Run the script:
   ```
   python pdf_to_word.py
   ```

5. The converted Word document will be saved at the specified location.

## Parameters

- `pdf_path`: Path to the input PDF file.
- `word_path`: Path to save the output Word document.

## Example

```python
from pdf2docx import Converter

def pdf_to_word(pdf_path, word_path):
    cv = Converter(pdf_path)
    cv.convert(word_path, start=0, end=None)
    cv.close()

if __name__ == "__main__":
    pdf_file_path = "path_to_pdf/file.pdf"
    word_file_path = "path_to_save_word_file/word.docx"

    pdf_to_word(pdf_file_path, word_file_path)
```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License] (LICENSE).

---
