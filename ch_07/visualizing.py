from pathlib import Path
import pandas as pd
import plotly.express as px
from folder import out_dir
from cumulratecalc import out_3_1

df_raw=pd.read_csv(out_3_1)
fig=px.treemap(
    df_raw,
    path=["종목명"],
    values="조단위",
    )
fig.update_traces(
    marker=dict(
        cornerradius=5,
        colorscale="Plasma",
        pad=dict(t=10,r=10,b=10,l=10)
    ),
    texttemplate="<b>%{label}</b><br>%{value:,.0f}조원",
    textfont_size=30
)

fig.update_layout(margin=dict(t=0,r=0,b=0,l=0))
img_path=out_dir/f"{Path(__file__).stem}.png"
fig.write_image(img_path,width=1600,height=900,scale=2)

