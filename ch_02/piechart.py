#데이터 프레임 분할
import pandas as pd
from pivottablefin import out_3_2

N=4
df_raw=pd.read_excel(out_3_2)
df_head,df_tail=df_raw.iloc[:N],df_raw.iloc[N:]
#행,열 숫자 인덱스로 선택
df_tail

#열별 합계
df_sum=df_tail.drop(columns=["분류"]).sum().to_frame().transpose()
#drop() 제거
#to_frame() 데이터 프레임으로 변환
#transpose 행, 열 전환
df_sum["분류"]="기타"
df_sum

#데이터 프레임 연결
df_final=pd.concat([df_head,df_sum],ignore_index=True)
df_final

#시각화
from pathlib import Path
import matplotlib.pyplot as plt
from folder import out_dir

values=df_final["누적금액"]

fig,ax=plt.subplots(figsize(16,9),dpi=100)
ax.pie(
    values,
    textprops=dict(color="black",size=20), #폰트설정
    startagle=90, #각도 설정
    autopct="%.1f%%", #비율 출력 형식 지정 #소수점 1번째 자리 %
)
fig.savefig(out_dir/f"{Path(__file__).stem}.png",bbox_inches="tight")