import pandas as pd;
from openpyxl import Workbook
from openpyxl import load_workbook
import numpy as npy
import re as re

ban_kan = pd.read_excel('Bangalore_to_Kannur.xlsx')
ban_koz = pd.read_excel('Bangalore_to_Kozhikode.xlsx')
ern_koz = pd.read_excel('Ernakulam_to_Kozhikode.xlsx')
koz_ban = pd.read_excel('Kozhikode_to_Bangalore.xlsx')
koz_ern = pd.read_excel('Kozhikode_to_Ernakulam.xlsx')
koz_mys = pd.read_excel('Kozhikode_to_Mysore.xlsx')
koz_tnv = pd.read_excel('Kozhikode_to_Thiruvananthapuram.xlsx')
koz_thr = pd.read_excel('Kozhikode_to_Thrissur.xlsx')
mys_koz = pd.read_excel('Mysore_to_Kozhikode.xlsx')
tnv_koz = pd.read_excel('Thiruvananthapuram_to_Kozhikode.xlsx')

result = pd.concat([ban_kan, ban_koz, ern_koz,koz_ban,koz_ern,koz_mys,koz_tnv,koz_thr,mys_koz,tnv_koz], ignore_index=True)
result = result.drop(columns=['Unnamed: 0'])

result['ID'] = result.index+1
print(result)

result.to_excel('kerala.xlsx',index=False)
# df = df.loc[:, ~df.columns.str.contains('^Unnamed')]