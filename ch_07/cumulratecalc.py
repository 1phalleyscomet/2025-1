from pathlib import Path
import pandas as pd
from folder import out_dir
from pagemovndatacollect import out_2_2

out_3_1=out_dir/f"{Path(__file__).stem}.csv"

def top_kospi_cimpany(df_raw:pd.DataFrame,prop:float)->pd.DataFrame:
    df_raw["시가총액"]=df_raw["시가총액"].str.replace(",","").astype(int)
    df_raw["조단위"]=df_raw["시가총액"]/10_000
    df_raw=df_raw.sort_values("시가총액",ascending=False) #내림차순 정렬
    df_raw["누적비율"]=df_raw["시가총액"].cumsum()/df_raw["시가총액"].sum()
    df_sliced=df_raw.loc[df_raw["누적비율"]<=prop] #슬라이싱
    return df_sliced.filter(["종목명","시가총액","조단위","누적비율"])

if __name__=="__main__":
    df_raw=pd.read_csv(out_2_2)
    df_top=top_kospi_cimpany(df_raw,0.5) #상위 50% 종목 추출
    df_top.to_csv(out_3_1,index=False)