from pathlib import Path
import qrcode
from fodler import out_dir

out_2_2_vcf=out_dir/f"{(__file__).stem}.vcf"
out_2_2_png=out_dir/f"{(__file__).stem}.png"

if __name__=="__main__":
    data=[
        "BEGIN:VCARD" #vcard 시작
        "VERSION:3.0"
        "N:Halley;Admond;;;" #성;이름;미들네임;접두어;접미어
        "FN: Admond Halley" #전체 이름
        "TEL;type=CELL:+82 10-1234-5678"
        "END: VCARD" #종료
    ]    
    vcf="\n".join(data)
with open(out_dir/f"{Path(__file__).stem}.vcf","w",encoding="utf-8") as fp:
    fp.write(vcf)

    img=qrcode.make(vcf)
    img.save(out_2_2_png)