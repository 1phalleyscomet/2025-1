from playwrightfunc import run_playwright
from inspectorrun import goto_best
from imgcap import take_screenshots
from optionselc import select_category,select_options

def fetch_trends_by_filter(category:str=None,option:str=None):
    play,browser,page=run_playwright(slow_mo=500)
    goto_best(page)
    if category:
        select_category(page,category)
        if option:
            select_options(page,option)
        take_screenshots(page)
        browser.close()
        play.stop()

if __name__=="__main__":
    category,option="패션의류","10대 여성"
    fetch_trends_by_filter(category,option)