from pathlib import Path
import matplotlib.pyplot as plt
from filesize import out_dir
from datapreprocessing import LoadPlotdata

PlotData=LoadPlotdata()
fig,ax=plt.subplots()
ax.barh(PlotData["stem"],PlotData["size"])
fig.savefig(out_dir/f"{Path(__file__)}.stem.png")