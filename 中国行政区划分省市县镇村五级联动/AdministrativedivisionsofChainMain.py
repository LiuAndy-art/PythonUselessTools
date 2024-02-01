import time
import pandas as pd
import sys
import os
df = pd.read_excel("2023年统计用区划代码和城乡划分代码省级URL.xlsx")

try:
    start = int(sys.argv[1])
except BaseException:
    start = 0

provinceurl = df["省份URL"].iloc[start]
citydf = pd.read_html(provinceurl)[-1].iloc[1:, ]
# 遍历每一个地级市
for j in range(citydf.shape[0]):
    os.system(
        "python AdministrativedivisionsofChinaVice.py {} {}".format(
            start,
            j))
    time.sleep(10)
