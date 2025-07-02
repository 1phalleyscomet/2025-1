from pathlib import Path
import pandas as pd
from folder import in_dir, out_dir

result=[]
for xlsx_path in Path(in_dir).glob("2024년*월.xlsx"):
    df_raw=pd.read_excel(xlsx_path,sheet_name="Sheet1",usecols="B:E",skiprows=2) #usecols="B:E" B열부터 E열까지 읽기
    result.append(df_raw)
result
df_concat=pd.concat(result)
df_concat.to_excel(out_dir/f"{Path(__file__).stem}.xlsx",index=False) #concat() 여러 데이터 프레임 연결 함수
#to_excel() 엑셀 파일로 저장