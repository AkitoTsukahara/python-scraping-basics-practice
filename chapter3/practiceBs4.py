import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

# リストを使ってエピソードの一覧を保存する
episodes = []

ep_tables = html_soup.find_all('table', class_='wikiepisodetable')

for table in ep_tables:
    headers = []
    rows = table.find_all('tr')
    #まず、フィールド名を決めるために最初の行からヘッダーのセルを取得する
    for header in table.find('tr').find_all('th'):
        headers.append(header.text)
    # 次に１行目を除く全ての行を処理する
    for row in table.find_all('tr')[1:]:
        values = []
        # 各列のセルを取得する。１つ目のタグはth
        for col in row.find_all(['th', 'td']):
            values.append(col.text)
            if values:
                episode_dict = {headers[i]: values[i] for i in
                range(len(values))}
                episodes.append(episode_dict)
# 結果を表示する
for episode in episodes:
    print(episode)