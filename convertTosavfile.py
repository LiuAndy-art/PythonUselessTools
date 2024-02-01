import pandas as pd
import pyreadstat

# 读取 CSV 数据集
csv_file_path = 'your_dataset.csv'
df = pd.read_csv(csv_file_path)
# 将 DataFrame 转换为 SPSS 数据集
sav_file_path = 'output_dataset.sav'
pyreadstat.write_sav(df, sav_file_path)
print(f"CSV 数据集已成功转换为 {sav_file_path}")
