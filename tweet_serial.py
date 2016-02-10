#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
from requests_oauthlib import OAuth1Session
import datetime

CK = '8QLpI4ZDmxx1ZYmUtKWBH4DN6'                             # Consumer Key
CS = 'zhd41KVW8h0riXmm6VDUzdJ66oTdBLXX6xDlnbNxu5Gq9oHQHV'         # Consumer Secret
AT = '265428880-scFjoTD06rsLcXiWzzPvSbQPWXlexWU0MVrPA1Nk' # Access Token
AS = 'CIb6cE2SaKLwFZILEvrWNLldONhnUQecflJGA6SxldT8C'         # Accesss Token Secert

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

if __name__ == '__main__':
    while True:
        res_serial = ser.read()
        print res_serial
        if res_serial == "1":
            now = datetime.datetime.now()
            msg = "部屋に誰か来たよ。\n" + now.strftime("%Y/%m/%d %H:%M:%S\n")
            tweet_content = msg + "\n from tweet.py"
            print tweet(tweet_content) 
