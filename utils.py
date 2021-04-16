import feedparser

def get_news(publication, RSS_FEEDS = None):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed['entries']