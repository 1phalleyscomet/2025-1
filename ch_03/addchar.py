from PIL import Image
from folder import img_dir
img=Image.open(img_dir/'img_001.jpg')
img

from PIL import ImageDraw

draw=ImageDraw.Draw(img)
draw.text(
    xy=(10,100),
    text="Hello World!",
    fill=(255,255,255),
    font_size=50, #코드 수정 용이
)
img

