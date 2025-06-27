from pathlib import Path
from filesize import work_dir #이전 작성 모듈 호출

def GetTotalFilesize(base_dir: Path, pattern: str="*") -> int: #type hint 변수 데이터 타입 사전 지정 #pattern: 글로브 패턴 문자열 저장
    total_bytes=0
    for fullpath in base_dir.glob(pattern): #glob() 글로브 패턴과 일차하는 파일명 리스트 반환
        if fullpath.is_file(): #is_file() 파일 유효 검사
            total_bytes += fullpath.stat().st_size #stat() 파일 상세 정보 표시 #st_size 파일 바이트 수
    return total_bytes

if __name__ =="__main__":
    base_dir=work_dir
    filesize=GetTotalFilesize(base_dir, pattern="*") #"*" 모든파일
    print(f"{base_dir.as_posix()=}, {filesize=} bytes") #as_posix 문자열 반환