import json
from pathlib import Path
import pandas as pd
from folder import out_dir
from finance import out_1_3

def clean_white_space(text:str)->str:
    return " ".join(text.split()) #공백 문자 정제

def table_to_dataframe(header:list,body:list)->pd.DataFrame:
    df_raw=pd.DataFrame(body,columns=header) #dataframe 객체 생성
    df_raw=df_raw.dropna(how="any") #하나의 열이라도 데이터가 없다면 행 삭제
    df_raw=df_raw.iloc[:,:-1] #마지막 열 삭제
    for col in df_raw.columns:
        df_raw[col]=df_raw[col].apply(clean_white_space) #열 별로 공백 문자 정제
    return df_raw

if __name__=="__main__":
    parsed=json.loads(out_1_3.read_text(encoding="utf-8"))
    header,body=parsed["header"],parsed["body"]
    df_raw=table_to_dataframe(header,body)
    df_raw.to_csv(out_dir/f"{Path(__file__).stem}.csv",index=False)
    