import praw
import requests
import json
import sys
from config import *

count_comments = 0
count_upvotes = 0
count_uniques = 0

uniques = set()

def get_all_threads():
    params = {"subreddit" : sys.argv[1],
            "filter" : "id",
            "sort" : "desc",
            "size" : "100000"}
    response = requests.get("https://api.pushshift.io/reddit/search/submission/", params=params)
    return response.json()

def organize_threads(response):
    threads = list()
    r = json.dumps(response)
    r = json.loads(r)
    if "data" in r:
        for i in xrange(0, len(r["data"])):
            threads.append(r["data"][i]["id"])
    threads = [str(item) for item in threads]
    return threads

response = get_all_threads()
posts = organize_threads(response)

print 'r/' + str(sys.argv[1]) + ' has ' + str(len(posts)) + ' posts till now.'

reddit = praw.Reddit(user_agent=USER_AGENT,
                     client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     username=USERNAME, password=PASSWORD)

for i in xrange(0, len(posts)):
    submission = reddit.submission(id=posts[i])
    count_comments = count_comments + int(submission.num_comments)
    count_upvotes = count_upvotes + int(submission.score)
    uniques.add(submission.author)
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        uniques.add(comment.author)

    count_uniques = len(uniques)

    print 'Total posts parsed: ' + str(i+1) + ', total comments: ' + str(count_comments) + ', total upvotes: ' + str(count_upvotes) + ', total unique participants: ' + str(len(uniques))

print 'r/' + str(sys.argv[1]) + ' has ' + str(count_comments) + ' comments in its posts.'
print 'r/' + str(sys.argv[1]) + ' has ' + str(count_upvotes) + ' upvotes in its posts.'
print 'r/' + str(sys.argv[1]) + ' has ' + str(count_uniques) + ' unique participants in its posts.'
