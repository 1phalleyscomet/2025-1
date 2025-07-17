from pathlib import Path

work_dir=Path(__file__).parent
out_dir=work_dir/"output"

if __name__=="__main__":
    out_dir.mkdir(exist_ok=True)