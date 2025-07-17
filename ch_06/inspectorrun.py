from playwright.sync_api import Page
from playwrightfunc import run_playwright

def goto_best(page:Page):
    page.goto("https://shopping.naver.com/ns/home")
    page.get_by_role("link", name="베스트 NONE").click()
    page.get_by_role("link", name="베스트상품").click()

if __name__=="__main__":
    play,browser,page=run_playwright(slow_mo=1000)
    goto_best(page)
    page.pause()
    browser.close()
    play.stop()