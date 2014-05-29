import praw
import re
import time

username = 'muchtipshibe'
password = 'Parciau'

r = praw.Reddit('you_get_doge')
r.login(username,password)

already_done = []


print 'starting...'

while True:

	subreddit = r.get_subreddit('dogecoin')

	for submission in subreddit.get_new(limit=20):

		print ('Checking...', submission.id)
		if submission.id not in already_done:
					submission.upvote()
					print ("upvoted! ", submission.id)
					submission.add_comment('To the mooooon! +/u/dogetipbot 4 doge')
					print ('replied! ', submission.id)
					already_done.append(submission.id)

	print ('sleeping for 10 seconds')
	time.sleep(10)
