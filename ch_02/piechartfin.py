from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from folder import out_dir
from pivottablefin import out_3_2

def load_data(n: int=4)->pd.DataFrame:
    df_raw=pd.read_excel(out_3_2)
    df_head,df_tail=df_raw.iloc[:n],df_raw.iloc[n:]
    df_sum=df_tail.drop(columns=["분류"]).sum().to_frame().transpose()
    df_sum["분류"]="기타"
    return pd.concat([df_head,df_sum],ignore_index=True)

if __name__=="__main__":
    df_raw=load_data()
    values = df_raw["누적금액"]
    fig,ax=plt.subplots(figsize=(16,9),dpi=100)
    ax.pie(
        values,
        textprops=dict(color="black",size=20), #폰트설정
        startangle=90, #각도 설정
        autopct="%.1f%%", #비율 출력 형식 지정 #소수점 1번째 자리 %
)
    fig.savefig(out_dir/f"{Path(__file__).stem}.png",bbox_inches="tight")

