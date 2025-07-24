import trafilatura

def extract_text_img(url:str)->tuple[str,str]:
    html=trafilatura.fetch_url(url)
    text=trafilatura.extract(
        html,
        output_format="markdown",
        include_comments=False,
    )
    img_url=trafilatura.extract_metadata(html).image
    return text, img_url

if __name__=="__main__":
    url="https://www.bbc.com/culture/article/20250721-intimate-images-of-the-real-hotel-california"
    text,img_url=extract_text_img(url)
    print(f"{text=}")
    print(f"{url=}")