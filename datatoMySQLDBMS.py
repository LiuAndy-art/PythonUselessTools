import pymysql
from SoEasyData import GetSeabornData as getdata
"""
一、连接mysql数据库
"""
# 打开数据库连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='******',
    charset='gbk',
    db='testdb',  # 数据库名称
)

# 使用cursor()方法获取操作游标
c = conn.cursor()

"""
二、读取excel文件
"""
df = getdata("iris")
cap = df.values.tolist()
"""
三、将读取到的数据批量插入数据库
"""
for Stu, j in zip(cap, range(len(cap))):
    ids = j+1
    Sno = Stu[0]
    Sname = Stu[1]
    Ssex = Stu[2]
    Sage = Stu[3]
    Sdept = Stu[4]
    print(f"insert into iris value ({ids}, {Sno}, {Sname}, {Ssex}, {Sage}, '{Sdept}')")
    # 使用f-string格式化字符串，对sql进行赋值
    c.execute(f"insert into iris value ({ids}, {Sno}, {Sname}, {Ssex}, {Sage}, '{Sdept}')")
conn.commit()
conn.close()
print("插入数据完成！")

# 创建表的语法
# -- 设置字符编码
# SET NAMES gbk;
# SET FOREIGN_KEY_CHECKS = 0;
# -- 若表没有不存在则不删除表，否则删除
# DROP TABLE IF EXISTS iris;
# CREATE TABLE iris (
#   id int(11) NOT NULL AUTO_INCREMENT,
#   sepal_length varchar(100) NOT NULL,
#   sepal_width varchar(100) NOT NULL,
#   petal_length varchar(100) NOT NULL,
#   petal_width varchar(100) NOT NULL,
#   species varchar(100) NOT NULL,
#   PRIMARY KEY (id)
# ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT character set = utf8;
