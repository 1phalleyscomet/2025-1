from qrcode.image.styledpil import StyledPilImage
from qrcode.main import QRCode
from fodler import in_dir
from vcffin import out_2_2_vcf

with open(out_2_2_vcf,encoding="utf-8") as fp:
    vcf=fp.read()

qr=QRCode()
qr.add_data(vcf)
img=qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path=in_dir/"phone.png",
)
img