import os
from PyPDF2 import PdfMerger

def combine_pdfs(input_folder, output_filename):
    pdf_merger = PdfMerger()

    # Get a list of all PDF files in the input folder
    pdf_files = [file for file in os.listdir(input_folder) if file.lower().endswith('.pdf')]

    # Sort the files to combine them in a specific order if needed
    pdf_files.sort()

    for pdf_file in pdf_files:
        file_path = os.path.join(input_folder, pdf_file)
        pdf_merger.append(file_path)

    # Automatically attach '.pdf' to the output file name if not already provided
    if not output_filename.endswith('.pdf'):
        output_filename += '.pdf'

    # Get the output file path in the same folder as the input folder
    output_path = os.path.join(input_folder, output_filename)

    # Write the merged PDF to the output file
    with open(output_path, 'wb') as output:
        pdf_merger.write(output)

    print(f"PDF files combined and saved as '{output_path}'.")

if __name__ == '__main__':
    input_folder = input("Enter the path to the folder with PDFs: ")
    output_filename = input("Enter the desired output file name: ")
    combine_pdfs(input_folder, output_filename)
