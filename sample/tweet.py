#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import os

# zshrcに記述
CK = os.environ["TWITTER_CK"]
CS = os.environ["TWITTER_CS"]
AT = os.environ["TWITTER_AT"]
AS = os.environ["TWITTER_AS"]

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
    print CK, CS ,AT ,AS
    msg = raw_input("ツイートを入力\n__>")
    tweet_content = msg + "\n from tweet.py"
    print tweet(tweet_content)
