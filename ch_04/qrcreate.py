import qrcode

img=qrcode.make("qr code!")
img

#페이지 연결
img_halley=qrcode.make(https://1phalleyscomet.tistory.com/)

#qr코드 파일로 저장
from pathlib import Path
from fodler import out_dir

img.save(out_dir/f"{Path(__file__).stem}.png")
img_halley.save(out_dir/f"{Path(__file__).stem}_halley.png")