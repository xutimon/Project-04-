import praw
import random
import time
reddit = praw.Reddit('bot')
subreddit=reddit.subreddit('cs40_2022fall')
post=list(reddit.subreddit('YangForPresidentHQ').hot(limit=None))
while True:
    submission=random.choice(post)
    title=submission.title
    selftext=submission.selftext
    try:
        if selftext == '':
            url=submission.url
            subreddit.submit(title, url=url)
        else:
            subreddit.submit(title, selftext=selftext)
    except praw.exceptions.RedditAPIException:
        pass

    time.sleep(3)

