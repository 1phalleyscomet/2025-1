from pathlib import Path
from PIL import Image
from fodler import in_dir,out_dir
from vcffin import out_2_2_png

out_3_2=out_dir/f"{Path(__file__).stem}.png"

if __name__=="__main__":
    qr=Image.open(out_2_2_png).convert("RGBA") 
    width_qr,heigth_qr=qr.size
    icon=Image.open(in_dir/"phone.png")
    width_icon=int(width_qr*0.2)
    heigth_icon=int(heigth_qr*0.2)
    icon_resized=icon.resize((width_icon,heigth_icon))

    pad=50
    icon_x=width_icon - width_icon - pad
    icon_y=heigth_qr - heigth_icon - pad

    qr.paste(icon_resized,box=(icon_x,icon_y),mask=icon_resized)
    qr.save(out_3_2)