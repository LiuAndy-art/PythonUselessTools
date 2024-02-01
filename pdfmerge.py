import PyPDF2


def merge_pdfs(input_paths, output_path):
    pdf_merger = PyPDF2.PdfMerger()

    for path in input_paths:
        pdf_merger.append(path)

    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)


# 示例用法
input_files = ['File1.pdf', 'File2.pdf']
output_file = 'merged_output.pdf'

merge_pdfs(input_files, output_file)
