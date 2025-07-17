import json
from pathlib import Path
from playwright.sync_api import Page
from playwrightfunc import run_playwright
from inspectorrun import goto_best
from folder import out_dir

out_2_2=out_dir/f"{Path(__file__).stem}.json"

def take_screenshots(page:Page,count:int=15):
    locs=page.locator("li[class*='productCardResponsive_product_card']").all()
    imgs_path=[]
    for idx,loc in enumerate(locs[:count]):
        path= out_dir/f'{Path(__file__).stem}_{idx+1:03}.png' #캡처 이미지 경로
        loc.screenshot(path=path)
        imgs_path.append(path.as_posix())
    with open(out_2_2,"w",encoding="utf-8")as fp:
        json.dump(imgs_path,fp,indent=2,ensure_ascii=False)

if __name__=="__main__":
    play,browser,page=run_playwright(slow_mo=1000)
    goto_best(page)
    page.pause()
    take_screenshots(page)
    browser.close()
    play.stop()

#inspector resume click!