from pathlib import Path

work_dir=Path(__file__).parent #__file__ 현재 파일의 절대 경로
out_dir=work_dir/"output"

if __name__=="__main__": #__name__ 확장자 제외 현 파일명
    out_dir.mkdir(exist_ok=True) #mkdir 디텍토리(folder) 생성