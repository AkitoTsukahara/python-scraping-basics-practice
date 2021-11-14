import unicodedata
import MeCab

# MeCabの設定
tagger =  MeCab.Tagger('-r /usr/local/etc/mecabrc')

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

# texts = [
#     "ビザスクでエンジニアとして働いています。",
#     "三菱UFJモルガンスタンレー証券とガーディアンアドバイザーズでの経歴",
#     "キャノン株式会社で経営監理を5年経験しました。",
# ]

texts = [
    "リアルワールド<3691>、「デジタルプラス」に商号変更　子会社REAL FINTECHの吸収合併を検討",
    "リアルワールド<3691>、ダブルスタンダード<3925>等3社と資本業務提携",
    "IBJ<6071>、事業ポートフォリオの最適化に向け方針を決議",
]

for text in texts:
    companies = extract_company(text)
    print("text: ", text)
    for company in companies:
        print("キーワード: {},  正式名称: {}".format(company[0], company[1]))