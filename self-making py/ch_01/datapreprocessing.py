import json
from pathlib import Path
from filesize import out_dir
from runfilesizeget import LoadFilesizePerDir

out_3_1=out_dir / f"{Path(__file__).stem}.json"

def DumpPlotData():
    SizePerPath=LoadFilesizePerDir()
    SizePerStem={Path(path).stem: size for path,
                 size in SizePerPath.items()
                 if size>0}
    PlotData=dict(
        stem=list(SizePerStem.keys()),
        size=list(SizePerStem.values()),
    )
    with open(out_3_1,"w",encoding="utf-8") as fp:
        json.dump(PlotData,fp, ensure_ascii=False,indent=2)

def LoadPlotdata()->dict:
    if out_3_1.is_file():
        with open(out_3_1,encoding="utf-8") as fp:
            return json.load(fp)
    return {}

if __name__=="__main__":
    DumpPlotData()