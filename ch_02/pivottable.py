import pandas as pd
from  datacollect2 import out_2_2

df_raw=pd.read_excel(out_2_2)
df_pivot_1=pd.pivot_table(df_raw,index="분류",values="사용금액",aggfunc="sum")
df_pivot_1
#index 행이 될 집계 기준 열
#colums 열이 될 집계 기준 열
#values 집계 데이터
#aggfunc 집계 방식

#집계 기준 추가
df_raw["거래연월"]=df_raw["거래일시"].str.slice(0,7)
df_raw

#피벗 테이블 추가
df_pivot_2=pd.pivot_table(df_raw,index="분류", columns="거래연월",values="사용금액",aggfunc="sum")
df_pivot_2["누적금액"]=df_pivot_2.sum(axis=1)
df_pivot_2

#데이터 정렬
df_sort=df_pivot_2.sort_values("누적금액",ascending=False)
df_sort

#인덱스를 열로 변환
df_reindex=df_sort.reset_index()
df_reindex

#엑셀 파일로 저장
from pathlib import Path
from folder import out_dir

df_reindex.to_excel(out_dir/f"{Path(__file__).stem}.xlsx",index=False,sheet_name="분류별누적금액")
#index=True 엑셀 파일에 인덱스 열이 첫번재 열로 저장
#index=False 인덱스 없이 데이터만 저장