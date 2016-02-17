#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
from requests_oauthlib import OAuth1Session
import datetime
import os

CK = os.environ["TWITTER_CK"]
CS = os.environ["TWITTER_CS"]
AT = os.environ["TWITTER_AT"]
AS = os.environ["TWITTER_AS"]

ser = serial.Serial("/dev/tty.usbmodem1421",9600)

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

def tweet_test():
    now = datetime.datetime.now()
    msg = "部屋に誰か来たよ。\n" + now.strftime("%Y/%m/%d %H:%M:%S\n")
    tweet_content = msg + "\n from tweet.py"
    print tweet(tweet_content)

def say_test():
    msg = "部屋に誰か来たよ"
    os.system("say "+ msg)

if __name__ == '__main__':
    while True:
        res_serial = ser.read()
        print res_serial
        if res_serial == "1":
            now = datetime.datetime.now()
            msg = "部屋に誰か来たよ。\n" + now.strftime("%Y/%m/%d %H:%M:%S\n")
            tweet_content = msg + "\n from tweet.py"
            print tweet(tweet_content) 
            say_test()
