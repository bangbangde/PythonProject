import os
import argparse
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path, output_folder):
    output_folder = output_folder or os.path.dirname(input_pdf_path)
    filename = os.path.splitext(os.path.basename(input_pdf_path))[0]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_reader = PdfReader(input_pdf_path)
    
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])

        output_pdf_path = os.path.join(output_folder, f'{filename}_{page_num + 1}.pdf')
        with open(output_pdf_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split a PDF file into individual pages.')
    parser.add_argument('input_pdf', type=str, help='Path to the input PDF file')
    parser.add_argument('--output_folder', type=str, help='Path to the output folder')

    args = parser.parse_args()
    split_pdf(args.input_pdf, args.output_folder)
    