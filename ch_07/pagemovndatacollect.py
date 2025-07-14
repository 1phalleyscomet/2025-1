from pathlib import Path
import pandas as pd
from playwright.sync_api import Page
from folder import out_dir
from playwrightfunc import run_playwright
from finance import goto_market_cap, parse_table_kospi
from datarefine import table_to_dataframe
from pagecount import fetch_total_page

out_2_2=out_dir/f"{Path(__file__).stem}.csv"

def goto_page(page:Page,to:int):
    page.goto(f"https://finance.naver.com/sise/sise_market_sum.naver?&page={to}")

def fetch_market_cap(page:Page)->pd.DataFrame:
    total_page=fetch_total_page(page)
    result=[]
    for to in range(1,total_page+1): #1~total_page 반복
        goto_page(page,to) #페이지 이동
        header,body=parse_table_kospi(page) #코스피 시가총액 표 추출
        df_raw=table_to_dataframe(header,body) #데이터 정제, dataframe 객체 생성
        result.append(df_raw) #df객체를 리스트에 임시저장
    return pd.concat(result) #df객체 결합

if __name__=="__main__":
    play,browser,page=run_playwright(slow_mo=1000)
    goto_market_cap(page) #시가총액 페이지로 이동
    df_result=fetch_market_cap(page)
    df_result.to_csv(out_2_2,index=False)
    browser.close()
    play.stop()

    