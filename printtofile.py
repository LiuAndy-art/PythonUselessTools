import sys

with open('./resultdata/resultoutput.txt', 'a') as file:
    # 重定向标准输出到文件
    sys.stdout = file
    # 打印到文件
    print("将输出结果保存到文件中，而不是直接输出到控制台！")
# 恢复标准输出
sys.stdout = sys.__stdout__
