
import pandas as pd
# df=pd.read_csv('E:/college/graduation/demo/house_price_predict/pre_data/test.csv',encoding='gbk') 
df=pd.read_csv('E:/college/graduation/demo/house_price_predict/pre_data/pre_data_optimized.csv',encoding='gbk') 
# df=pd.read_csv('E:/college/graduation/demo/house_price_predict/pre_data/pre_data.csv',usecols=['district','bedroomNum','livingroomNum','bathroomNum','area','builtYear','direction','distance2SW','floorNum','type','price'],encoding='gbk') 

print(df.dtypes)
print(df.head())     #查看引入的csv文件前5行数据

# #---------------------------------------------------------------------#
# #-----------------------------提取小数---------------------------------#
# df["area"]= df["area"].str.extract('(\d+(?:\.\d+)?)', expand=False)
# df["area"].astype(float)
# print(df['area'])
# #-----------------------------提取整数---------------------------------#
# df["builtYear"]= df["builtYear"].str.extract('(\d+)', expand=False)
# #df["builtYear"].astype(int)
# print(df['builtYear'])

