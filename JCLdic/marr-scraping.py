import unicodedata
import MeCab
import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import date

# MeCabの設定
tagger =  MeCab.Tagger('-r /usr/local/etc/mecabrc')
# sqliteの設定
conn = sqlite3.connect('JCLdic/marr_scraping.db')
conect = conn.cursor()

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

# 登録されれいる会社名を検索する
def matched_companies(name):
    result = conect.execute('''
        SELECT id, name FROM companies
        WHERE name=:name
        ''', { 'name': name }).fetchall()
    return len(result) != 0

# スクレピング対象
url = 'https://www.marr.jp/mainfo/news/' + get_url_month()
data_list = get_title_and_links(url)

# 取得したデータ内から登録企業を検索・表示
for data in data_list:
    companies = extract_company(data['title'])
    for company in companies:
        
        if matched_companies(company[1]):
            print(company[1])
            print(data['title'])
            print(data['url'])

conn.close()