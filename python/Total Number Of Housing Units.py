import pandas as pd

df=pd.read_excel(r'E:\\Data_analysis_projects\\Total Number Of Housing Units\dataset\\housing_units_completed_us.xlsx')
df['sum']=df['south']+df['west']+df['midwest']+df['northeast']
df1=df.groupby('year')['sum'].sum()
df2=df.pivot_table(index='year',columns=None,values='sum',aggfunc='sum')

print(df1)
print(df2)