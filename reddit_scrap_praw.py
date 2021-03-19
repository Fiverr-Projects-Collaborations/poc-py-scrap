# Create keys here:  https://www.reddit.com/prefs/apps
# pip install praw
import praw
reddit_api = praw.Reddit(client_id='ABC', client_secret='XYZ', user_agent='personal')
top_posts = reddit_api.subreddit('wallstreetbets').top('month', limit=10)

# some fields to extract from all data
fields = ('id', 'title', 'url', 'score', 'created_utc', 'num_comments')
list_of_items = []
for submission in top_posts:
    to_dict = vars(submission)
    sub_dict = {field: to_dict[field] for field in fields}
    list_of_items.append(sub_dict)
print(list_of_items[0])
