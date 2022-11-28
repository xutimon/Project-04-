import praw
import random
import time
reddit = praw.Reddit('bot')
subreddit=reddit.subreddit('cs40_2022fall')
post=list(reddit.subreddit('YangForPresidentHQ').hot(limit=None))
while True:
    submission=random.choice(post)
    title=submission.title
    content=submission.selftext
    try:
        if content == '':
            link=submission.url
            subreddit.submit(title, url=link)
        else:
            subreddit.submit(title, selftext=content)
    except praw.exceptions.RedditAPIException:
        pass

    time.sleep(3)

