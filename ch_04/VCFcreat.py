#VCF: 전자명함 세계 표준
from pathlib import Path
from fodler import out_dir

data=[
    "BEGIN:VCARD" #vcard 시작
    "VERSION:3.0"
    "N:Halley;Admond;;;" #성;이름;미들네임;접두어;접미어
    "FN: Admond Halley" #전체 이름
    "TEL;type=CELL:+82 10-1234-5678"
    "END: VCARD" #종료
] 

vcf="\n".join(data) #리스트를 하나의 문자열도 변경
with open(out_dir/f"{Path(__file__).stem}.vcf","w",encoding="utf-8") as fp:
    fp.write(vcf)

import qrcode

img=qrcode.make(vcf)
img