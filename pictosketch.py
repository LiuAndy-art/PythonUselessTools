# 图像转换，将彩色图片转为素描风格
import cv2


inputfile = "a.png"
outputfile = "sketch.jpg"
# 读取图片
img = cv2.imread(inputfile)
# 灰度
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey)
# 高斯滤波
blur_img = cv2.GaussianBlur(invert, (7, 7), 0)
inverse_blur = cv2.bitwise_not(blur_img)
sketch_img = cv2.divide(grey, inverse_blur, scale=256.0)
# 保存
cv2.imwrite(outputfile, sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
