import praw
import re
import time

username = 'much_help'
password = 'datfakepassword'

r = praw.Reddit('you_get_doge')
r.config._ssl_url = None
r.login(username,password)

already_done = []

def msg(karma):
	msg = '''
Thanks for making a good post to /r/dogecoin, looks like it's gaining some upvotes!

Here, exchange those votes for Doge: +/u/dogetipbot %s doge


---

Beep Beep! Im a bot, if you have any problems, you can message me, /u/ieuang, or /u/addm3plz.
''' % str(karma)
	return msg

print 'starting...'

while True:
	subreddit = r.get_subreddit('dogecoin')
	for submission in subreddit.get_new(limit=10):
		print 'Checking...'
		if submission.id not in already_done:
			karma = submission.ups - submission.downs
			if float(karma) >= float(5):
				submission.upvote()
				print "upvoted!"
				submission.add_comment(msg(karma))
				print 'replied!'
				already_done.append(submission.id)
				
	print 'sleeping'
	time.sleep(200)
