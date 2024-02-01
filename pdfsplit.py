import PyPDF2

def split_pdf(input_path, output_path, start_page, end_page):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)

        # 确保开始和结束页码在有效范围内
        start_page = max(0, min(start_page, total_pages - 1))
        end_page = max(start_page, min(end_page, total_pages - 1))

        # 创建一个新的PdfFileWriter对象
        pdf_writer = PyPDF2.PdfWriter()

        # 从输入PDF中复制指定页码的内容到新的PDF
        for page_num in range(start_page, end_page + 1):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # 将新的PDF写入输出文件
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)


input_path = "1_单面两份.pdf"  # 输入PDF文件路径
output_path = "参与学术会议资料.pdf"  # 输出PDF文件路径
start_page = 1  # 开始页码（从0开始计数）
end_page = 4  # 结束页码
split_pdf(input_path, output_path, start_page, end_page)
