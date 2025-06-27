import json
from pathlib import Path
from filesize import out_dir
from savefilelist import GetTotalFilesize
from filesizeget import load_dirnames

out_2_4 = out_dir / f"{Path(__file__).stem}.json"

def DumpFilesizeFormDirnames():
    dirs=load_dirnames()
    result={} #dict result 생성, key:경로,value:크기
    for path_str in dirs:
        path=Path(path_str)
        filesize=GetTotalFilesize(path,pattern="**/*") #"**/*" 현재경로 및 모든 하위 경로
        result[path.as_posix()]=filesize
    with open(out_2_4,"w",encoding="utf-8") as fp:
        json.dump(result,fp,ensure_ascii=False,indent=2) 

def LordFilesizePerDir()->dict[str,int]:
    if out_2_4.is_file():
        with open(out_2_4, encoding="utf-8") as fp:
            return json.load(fp)
        return {}
if __name__=="__main__":
    DumpFilesizeFormDirnames()