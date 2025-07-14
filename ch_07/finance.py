import json
from pathlib import Path
from playwright.sync_api import Page
from folder import out_dir
from playwrightfunc import run_playwright

out_1_3=out_dir/f"{Path(__file__).stem}.json"

def goto_market_cap(page:Page):
    page.goto("https://finance.naver.com/")
    page.get_by_role("link",name="국내증시").click()
    page.get_by_role("link",name="시가총액",exact=True).first.click()

def parse_table_kospi(page:Page)->tuple[list,list]:
    tag_table=page.locator("table",has_text="코스피") #코스피 시가총액 표
    tag_thead=tag_table.locator("thead>tr>th")  #헤더 열
    header=tag_thead.all_inner_texts()
    tag_tbody=tag_table.locator("tbody>tr") #보디 행
    body=[tr.locator("td").all_inner_texts() for tr in tag_tbody.all()]
    return header, body

if __name__=="__main__":
    play,browser,page=run_playwright(slow_mo=1000)
    goto_market_cap(page) #시가총액 페이지로 이동
    header,body=parse_table_kospi(page) #코스피 시가총액 데이터 수집
    dumped=json.dumps(dict(header=header, body=body),ensure_ascii=False,indent=2)

    out_1_3.write_text(dumped,encoding="utf-8")
    browser.close()
    play.stop()

    