from PIL import Image, ImageOps
from folder import in_dir,out_dir

SIZE=(500,500)
img=Image.open(in_dir/"img_001.jpg")
img.resize(SIZE).save(out_dir/"1_resize.jpg") #이미지 비율 변경
ImageOps.conatain(img,SIZE).save(out_dir/"2_contain.jpg") #이미지가 요청한 크기보다 작을 수 있음(y축 기준 맞춤)
ImageOps.cover(img,SIZE).save(out_dir/"3_cover.jpg") #이미지가 요청한 크기보다 클 수 있음(x축 기준 맞춤)
ImageOps.fit(img,SIZE).save(out_dir/"4_fit.jpg") #이미지 일부가 잘릴 수 있음
ImageOps.pad(img,SIZE,color=(0,0,0)).save(out_dir/"5_pad.jpg") #크기 변경 후 남은 부분 지정된 색으로 채움