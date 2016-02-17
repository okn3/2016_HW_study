#coding: utf-8
"""

pythonからSlackAPI叩く

ref:http://kazu22002.hatenablog.com/entry/2015/04/20/003345

"""

import urllib
import urllib2

url = "https://slack.com/api/chat.postMessage"

params = {'token':'xoxp-3597322341-3611854702-21386437680-2c07b2bb6c',   # トークン
          'channel':'G04DKAC3W', # チャンネルID
          'text': 'test',    # 送信するテキスト
          'username':'okuno', # ユーザ名
}

params['text'] = 'test'
params = urllib.urlencode(params)

req = urllib2.Request(url)
# ヘッダ追加
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
# パラメータ追加
req.add_data(params)

res = urllib2.urlopen(req)

# レスポンス取得
body = res.read()
