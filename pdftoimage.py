from pdf2image import convert_from_path

# 将 PDF 转换为图像
images = convert_from_path('../概率空间.pdf', dpi=72)

# 保存图像
for i, image in enumerate(images):
    image.save(f'output{i+1}.png', 'PNG')
