import sys
import praw
from praw.models import MoreComments
from config import *

uniques_one = set()
uniques_two = set()
overlaps = set()

reddit = praw.Reddit(user_agent=USER_AGENT,
                     client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     username=USERNAME, password=PASSWORD)

submission_one = reddit.submission(url=sys.argv[1])

submission_one.comments.replace_more(limit=None)
for comment in submission_one.comments.list():
    uniques_one.add(comment.author)

submission_two = reddit.submission(url=sys.argv[2])
submission_two.comments.replace_more(limit=None)
for comment in submission_two.comments.list():
    uniques_two.add(comment.author)

overlaps = uniques_one & uniques_two

print '[x] There are ' + str(len(overlaps)) + ' unique participants that participated in both threads.'
