from pathlib import Path

work_dir=Path(__file__).parent
in_dir=work_dir/"input"

if __name__=="__main__":
    in_dir.mkdir(exist_ok=True)