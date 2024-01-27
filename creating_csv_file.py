'''
    Output as a json file 
'''

# {
#    "tweet_url":"https://twitter.com/elonmusk/status/1647298658331770883",
#    "name":"Elon Musk",
#    "user_id":"44196397",
#    "username":"elonmusk",
#    "published_at":"Sat Apr 15 17:59:40 +0000 2023",
#    "content":"Your direct experience, people you talk to in the subject area &amp; independent research will get you much closer to the truth",
#    "views_count":"7073534",
#    "retweet_count":12977,
#    "likes":124877,
#    "quote_count":526,
#    "reply_count":3455,
#    "bookmarks_count":569
# }


#This should be converted to a .csv file 

'''  
    So first we'll generate the file name, using the timestamp in Unix format, and the username from which to retrieve the tweets:

'''

import datetime
timestamp = int(datetime.datetime.now().timestamp())
filename = '%s_%s.csv' % (self.username, timestamp)
print('[+] writing %s' % filename)

'''
    And finally, we will use a DictWriter to elegantly convert our JSON dictionaries into .csv lines, as follows:
'''

with open(filename, 'w') as f:
    writer = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter='\t')
    writer.writeheader()

    for tweet in tweets: 
        print(tweet['id'], tweet['published_at'])
        writer.writerow(tweet)

