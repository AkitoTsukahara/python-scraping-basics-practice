import requests

url = 'http://www.webscrapingfordatascience.com/basichttp/'
r = requests.get(url)
print(r.text)
# サーバーから返却されたHTTpステータスコード
print(r.status_code)
# テキストのステータスメッセージ
print(r.reason)
# HTTPレスポンスヘッダー
print(r.headers)
# リクエスト情報はr.rquestにPythonオブジェクトとして保存される
print(r.request)
# HTTPリクエストヘッダーは？
print(r.request.headers)
# HTTPレスポンスのコンテンツ
print(r.text)