import vobject

vcard=vobject.vCard()
fn=vcard.add("FN")
fn.value="admond halley"
name=vcard.add("N")
name.value=vobject.vcard.Name(family="halley",given="admond")

tel_cell=vcard.add("TEL")
tel_cell.value="+82 1234-5678"
tel_cell.type_param='CELL'
tel_work=vcard.add("TEL")
tel_work.value="+82 9876-5432"
tel_work.type_param="WORK"

email=vcard.add("EMAIL")
email.value="email@example.com"
email.type_param="WORK"

title=vcard.add("TITLE")
title.value="scientist"

org=vcard.add("ORG")
org.value=["(직장)","(부서)"]

url=vcard.add("URL")
url.value="https://1phalleyscomet.tistory.com/"
print(vcard.serialize())

from pathlib import Path
from fodler import out_dir

with open(out_dir/f"{Path(__file__).stem}.vcf","w",encoding="utf-8") as fp:
    fp.write(vcard.serialize())

import qrcode
qr=qrcode.make(vcard.serialize())
