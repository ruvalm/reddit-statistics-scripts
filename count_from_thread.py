import sys
import praw
from praw.models import MoreComments
from config import *

uniques = set()

reddit = praw.Reddit(user_agent=USER_AGENT,
                     client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     username=USERNAME, password=PASSWORD)

submission = reddit.submission(url=sys.argv[1])

submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    uniques.add(comment.author)

print 'Thread has ' + str(submission.score) + ' upvotes.'
print 'Thread has ' + str(submission.num_comments) + ' comments.'
print 'Thread had ' + str(len(uniques)) + ' unique participants.'
