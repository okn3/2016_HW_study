#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session

CK = '8QLpI4ZDmxx1ZYmUtKWBH4DN6'                             # Consumer Key
CS = 'zhd41KVW8h0riXmm6VDUzdJ66oTdBLXX6xDlnbNxu5Gq9oHQHV'         # Consumer Secret
AT = '265428880-scFjoTD06rsLcXiWzzPvSbQPWXlexWU0MVrPA1Nk' # Access Token
AS = 'CIb6cE2SaKLwFZILEvrWNLldONhnUQecflJGA6SxldT8C'         # Accesss Token Secert

# ツイート投稿用のURL
URL = "https://api.twitter.com/1.1/statuses/update.json"

def tweet(text):
    #Tweetを作成
    params = {"status": text}

    # OAuth認証して、POSTで投稿
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.post(URL, params = params)

    #レスポンスコードを返す
    return req.status_code

if __name__ == '__main__':
    msg = raw_input("ツイートを入力\n__>")
    tweet_content = msg + "\n from tweet.py"
    print tweet(tweet_content)
