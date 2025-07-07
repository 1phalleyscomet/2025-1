from PIL import Image
from folder import img_dir
SIZE=(500,500)
img=Image.open(img_dir/'img_001.jpg')
img_resize=img.resize(SIZE)
img_black=Image.new(mode="RGBA",size=SIZE,color=(0,0,0,153))
img_comp=Image.alpha_composite(img_resize.convert("RGBA"),img_black)
img_comp