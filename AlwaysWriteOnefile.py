# 需求：有一个脚本文件script.py，它接受参数并且写入结果。
# 1. 我们希望它每隔n条就写入一个文件
# 2. 但不希望每次都手动输入参数
# 3. 并且要求每次执行一个参数输入，即顺序执行不适用for循环
# 4. 这个过程使用while True循环实现

import os
import time
import sys

try:
    group = sys.argv[1]
except BaseException:
    group = 1

count = 0
each = 10
while True:
    if os.path.exists(
        "第{}组第{}到第{}条数据.pkl".format(
            group,
            count + 1,
            count + each)):
        print(
            "正在运行第{}到第{}条数据......".format(
                count + each + 1,
                count + 2 * each))
        os.system(
            "python scripy.py {} {} {}".format(
                group, count + each, each))
        print("第{}到第{}条数据运行结束！！！".format(count + each + 1, count + 2 * each))
        count += each
    elif count == 0:
        print("正在运行第{}到第{}条数据......".format(count + 1, count + each))
        os.system("python scripy.py {} {} {}".format(group, count, each))
        print("第{}到第{}条数据运行结束！！！".format(count + 1, count + each))
    else:
        pass
    time.sleep(1)
