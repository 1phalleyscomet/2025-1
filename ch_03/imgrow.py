from PIL import Image, ImageOps
from folder import img_dir,out_dir
from pathlib import Path

rows,cols=1,8
w_img,h_img=500,500 #개별 이미지 크기
w_bg,h_bg=cols*w_img,rows*h_img #배경 이미지 크기
start_x,start_y=0,0 #개별 이미지 시작점 좌표
img_bg=Image.new(mode="RGB",size=(w_bg,h_bg))
path_sorted=sorted(Path(img_dir).glob("*.jpg"))
for path in path_sorted:
    img=Image.open(path)
    img_fit=ImageOps.fit(img,(w_img,h_img))
    img_bg.paste(img_fit,box=(start_x,start_y))
    start_x += w_img

img_bg.save(out_dir/f"{Path(__file__).stem}.jpg")