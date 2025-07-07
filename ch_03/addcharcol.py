from PIL import Image, ImageDraw, ImageFont
from folder import in_dir,out_dir
from pathlib import Path
from imgcol import out_3_2

img_raw=Image.open(out_3_2)

text="hello world"
font=ImageFont.truetype(in_dir/ "batang.ttc",size=100)
left,top,right,bottom=font.getbbox(text)

pad=20 #padding 과의 차이?
bg_width=pad+right+pad
bg_height=pad+bottom+pad

img_bg=Image.new("RGBA",size=img_raw.size)
draw_bg=ImageDraw.Draw(img_bg)
draw_bg.rectangle(xy=(0,0,bg_width,bg_height),fill=(0,0,0,200))

img_final=Image.alpha_composite(img_raw.convert("RGBA"),img_bg)
draw_final=ImageDraw.Draw(img_final)
draw_final.text(xy=(pad,pad),text=text,fill=(255,255,255),font=font)

img_final.convert("RGB").save(out_dir/f"{Path(__file__).stem}.jpg")