from pathlib import Path

work_dir=Path(__file__).parent
img_dir,in_dir,out_dir=work_dir/"img",work_dir/"input",work_dir/"output"

if __name__=="__main__":
    img_dir.mkdir(exist_ok=True)
    in_dir.mkdir(exist_ok=True)
    out_dir.mkdir(exist_ok=True)