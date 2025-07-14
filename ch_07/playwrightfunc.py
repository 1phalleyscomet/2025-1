from playwright.sync_api import Browser, Page, Playwright, sync_playwright

def run_playwright(slow_mo: float=None)->tuple[Playwright,Browser,Page]:
    play: Playwright=sync_playwright().start() #playwritght 객체 생성
    browser:Browser=play.chromium.launch(
        args=["--start-maximized"], #웹브라우저 최대화
        headless=False, #헤드리스 모드 사용 여부
        slow_mo=slow_mo, #자동화 처리 지연 시간
    )
    page:Page=browser.new_page(no_viewport=True) #page 객체 생성
    return play,browser, page


if __name__=="__main__":
    play,browser,page=run_playwright()
    page.goto("https://finance.naver.com/")
    page.pause()
    browser.close()
    play.stop()
