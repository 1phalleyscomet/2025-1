import json
from pathlib import Path
from filesize import out_dir

out_2_3=out_dir / f"{Path(__file__).stem}.json"

def dump_dirnames(base_dir:Path) -> None:
    dirs=[] #리스트 초기화
    for path in base_dir.iterdir(): #iterdir() 폴더의 모든 파일과 하위 폴더 목록 반환
        if path.is_dir(): #is_dir() 입력값이 디렉토리인지 확인
            dirs.append(path.as_posix())
    dirs_sorted=sorted(dirs) 
    with open(out_2_3, "w",encoding="utf-8") as fp: #변수 fp에 저장 
        json.dump(dirs_sorted, fp, ensure_ascii=False,indent=2) #dump() 데이터 상태 저장 
        #ensure_ascii=False 한글 문자열 아스키 반환 변경 방지
        #indent 공백 (tap)

def load_dirnames()->list[str]:
    if out_2_3.is_file():
        with open(out_2_3, encoding="utf-8") as fp:
            return json.load(fp)
    return []

if __name__=="__main__":
    dump_dirnames(Path.home())
