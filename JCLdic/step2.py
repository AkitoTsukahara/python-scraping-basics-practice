import unicodedata
import MeCab
import requests
from bs4 import BeautifulSoup
from datetime import date

# MeCabの設定
tagger =  MeCab.Tagger('-r /usr/local/etc/mecabrc')

# 実行時の年月を取得
def get_url_month():
    todays_date = date.today()
    return str(todays_date.year) + str(todays_date.month)

# スクレイピング
def get_title_and_links(url):
    html = requests.get(url).text
    html_soup = BeautifulSoup(html, 'html.parser')
    news_list = html_soup.find(class_='maFlashNewsList')
    links = []
    for index, news in enumerate(news_list.find_all("a")):
        links.append({ 'url': news.get('href'), 'title': news.text })
    return links

# テキストから企業名を抽出
def extract_company(text):
    # textのnormalize
    text = unicodedata.normalize('NFKC', text) 
    node = tagger.parseToNode(text)
    result = []
    while node:
        features = node.feature.split(',')
        if features[2] == '組織':
            result.append(
                (node.surface, features[6])
            )
        node = node.next
    return result

# スクレピング対象
url = 'https://www.marr.jp/mainfo/news/' + get_url_month()
data_list = get_title_and_links(url)

# 取得したデータ内から登録企業を検索・表示
for data in data_list:
    companies = extract_company(data['title'])
    print(companies)