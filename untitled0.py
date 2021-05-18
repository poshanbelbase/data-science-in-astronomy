import pandas as pd
df=pd.read_excel(r'D:\Astrolab\pythonproject\rawdata.xlsx')
#print(df.head(5))
#print(df)
df.drop(['name'],axis=1,inplace= True)
df.drop([0,1,2],0,inplace= True)
df['phasefirst']=df['JD(T)']-2456309.2695
df['phase']=df['phasefirst']/1.6797
df['var-c1']=df['var']-df['c1']
print(df['phase'])