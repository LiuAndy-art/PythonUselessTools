from PIL import Image
from pix2tex.cli import LatexOCR

# 将数学公式识别为latex语法的公式
img = Image.open('b.png')
model = LatexOCR()
print(model(img))
