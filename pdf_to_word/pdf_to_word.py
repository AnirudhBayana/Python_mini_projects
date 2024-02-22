from pdf2docx import Converter

def pdf_to_word(pdf_path, word_path):
    cv = Converter(pdf_path)
    cv.convert(word_path, start=0, end=None)
    cv.close()

if __name__ == "__main__":
    pdf_file_path = "path_to_pdf/file.pdf"
    word_file_path = "path_to_save_word_file/word.docx"

    pdf_to_word(pdf_file_path, word_file_path)
