from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from filesize import out_dir
from datapreprocessing import LoadPlotdata

PlotData=LoadPlotdata()
LogSize=np.log(PlotData["size"])
fig, ax=plt.subplots(figsize=(16,9),dpi=100)
ax.barh(PlotData["stem"], LogSize)
ax.grid(True,axis="x") #축 그리드
ax.tick_params(labelbottom=False, length=0,labelsize=20) #축 눈금
fig.set_layout_engine("tight")
fig.savefig(out_dir/f"{Path(__file__).stem}.png")