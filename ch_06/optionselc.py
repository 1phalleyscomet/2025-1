from playwright.sync_api import Page
from playwrightfunc import run_playwright
from inspectorrun import goto_best

def select_category(page:Page,category:str=None):
    selector="li[class*='imageCategoryResponsive_list']>button"
    page.locator(selector, has_text=category).click()

def select_options(page:Page,option:str=None):
    page.get_by_role("button", name="모두가 좋아하는 레이어 열기").click()
    page.get_by_text("10대 여성").click()

if __name__=="__main__":
    play,browser,page=run_playwright(slow_mo=1000)
    goto_best(page)
    select_category(page, "패션의류")
    select_options(page,"10대 여성")
    page.pause()
    browser.close()
    play.stop()
