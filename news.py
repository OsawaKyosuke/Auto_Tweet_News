# Twitter APIのライブラリをインポート
import tweepy
import datetime
import schedule
import time

# RSSフィードを解析するためのライブラリをインポート
import feedparser

# Twitter APIを使用するための認証情報を設定
api_key = "YOURKEY"
api_secret = "YOURKEY"
access_token = "YOURKEY"
access_token_secret = "YOURKEY"

# 認証情報を使用してTwitter APIへアクセス
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Yahoo JapanのニュースのRSSフィードのURL
feed_url = "https://news.yahoo.co.jp/rss/topics/top-picks.xml"

def getnews():
    global feed_url
    # RSSフィードを解析
    feed = feedparser.parse(feed_url)

    # 取得したニュースの見出しを使用して、Twitterに投稿
    api.update_status(f"【現在のニュース】\n\n1. {feed.entries[0].title if len(feed.entries) >= 1 else ''}\n2. {feed.entries[1].title if len(feed.entries) >= 2 else ''}\n3. {feed.entries[2].title if len(feed.entries) >= 3 else ''}\n\n" + "引用元（https://news.yahoo.co.jp/rss/topics/top-picks.xml）")


schedule.every().day.at("21:00").do(getnews)

while True:
  schedule.run_pending()
  time.sleep(1)
