from bs4 import BeautifulSoup


def extract_string_from_html(html_txt: str):
    parsed_txt = BeautifulSoup(html_txt, 'html.parser')
    return parsed_txt.title.string


html_txt = "<html><head><title>Why So Serious</title></head><body></body></html>"

soup = extract_string_from_html(html_txt)
print(soup)
