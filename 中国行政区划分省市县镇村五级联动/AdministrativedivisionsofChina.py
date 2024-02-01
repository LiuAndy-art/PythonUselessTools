import pickle
import time
import pandas as pd
import sys
import os
df = pd.read_excel("2023年统计用区划代码和城乡划分代码省级URL.xlsx")
count = 1
try:
    start = int(sys.argv[1])
except BaseException:
    start = 0

# 遍历每一个省份
# for i in range(start, df.shape[0]):
provinceurl = df["省份URL"].iloc[start]
citydf = pd.read_html(provinceurl)[-1].iloc[1:, ]
# 遍历每一个地级市
for j in range(citydf.shape[0]):
    mainurl = provinceurl.split(".html")[0]
    # 前四位
    cityend = citydf.iloc[j, 0][:4]
    cityurl = mainurl + "/" + cityend + ".html"
    if mainurl[-2:] == "11" or mainurl[-2:] == "12" or mainurl[-2:] == "31" or mainurl[-2:] == "50":
        try:
            areadf = pd.read_html(cityurl)[-1].iloc[1:,]
        except BaseException:
            continue
    else:
        try:
            areadf = pd.read_html(cityurl)[-1].iloc[2:,]
        except BaseException:
            continue
    # 遍历每一个区县级市
    for k in range(areadf.shape[0]):
        areaend = areadf.iloc[k, 0][:6]
        areaurl = mainurl + "/" + cityend[-2:] + "/" + areaend + ".html"
        try:
            towndf = pd.read_html(areaurl)[-1].iloc[1:,]
        except BaseException:
            continue
        for t in range(towndf.shape[0]):
            townend = towndf.iloc[t, 0][:9]
            townurl = mainurl + "/" + \
                cityend[-2:] + "/" + areaend[-2:] + "/" + townend + ".html"
            try:
                streetdf = pd.read_html(townurl)[-1].iloc[1:, ]
            except BaseException:
                continue
            length = len(streetdf.iloc[:, 2])
            res = pd.DataFrame({
                "省直辖市": [df.iloc[start, 1]] * length,
                "地级市": [citydf.iloc[j, 1]] * length,
                "区县级市": [areadf.iloc[k, 1]] * length,
                "乡镇街道": [towndf.iloc[t, 1]] * length,
                "村居委会": streetdf.iloc[:, 2].values.tolist()
            })
            print(res)
            if not os.path.exists(
                    "./generate/{}".format(df["省份"].iloc[start])):
                os.makedirs("./generate/{}".format(df["省份"].iloc[start]))
            with open("./generate/{}/第{}个行政区划分地址.pkl".format(df["省份"].iloc[start], count), "wb") as fp:
                pickle.dump(res, fp)
            count += 1
            time.sleep(1)
        time.sleep(1)
    time.sleep(1)
