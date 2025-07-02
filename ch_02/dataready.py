import pandas as pd
from folder import in_dir

df_raw=pd.read_excel(in_dir/"2024년1월.xlsx",sheet_name="Sheet1",usecols="B:E",skiprows=2)
df_raw