from PIL import Image
from folder import img_dir

img=Image.open(img_dir/"img_001.jpg")
print(f"{img.size=},{img.format=},{img.mode=}")

#size change
SIZE=(500,500)
img_resize=img.resize(SIZE)
print(f"{img_resize.size=}")
img_resize

#비율유지
from PIL import ImageOps

img_cont=ImageOps.contain(img,SIZE)
print(f"{img_cont.size=}")
img_cont