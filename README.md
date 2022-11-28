# Project-04

The name of my bot is throwaway_bot223. The bot.py file generates comments and replies in support of former presidential candidate Andrew Yang. For this project, I believe that my score should be 31/30. Below will be the task breakdown. 

# Required Tasks 
I have completed every task in bot.py (12 points). 
I have competed the github repo (3 points). 
I have posted 1000 valid comments (10 points). 



# Optional Tasks 
I have posted >200 submissions from the subreddit r/YangForPresidentHQ (2 points). 
I have created an army of 5 bots, all posting >500 comments. The bots are throwaway_bot223, throwaway_bot224, throwaway_bot225, throwaway_bot226 and throwaway_bot227 (2 points). 
I have made it possible for my bot to reply to the most highly upvoted comment instead of just a random comment. In the bot.py file, the code is currently commented out, but I have tested and it works. To run it, you simply have to replace the existing answer for task 4 with the following commented-out code (2 points):
```
        comments_without_replies.sort(key=lambda x:x.score, reverse = True)
        try:
            comments_without_replies[0].reply(generate_comment())
        except IndexError:
            pass
        except praw.exceptions.RedditAPIException:
            pass
```




#Favorite Thread
My favorite thread is the following

