# API info : https://github.com/pushshift/api
import requests
import json
list_of_items = []

#Fetch submissions
extract_api_url = 'https://api.pushshift.io/reddit/search/submission/' \
                  '?subreddit=SUBREDDIT' \
                  '&after=START_DATE' \
                  '&size=100' \
                  '&fields=FIELDS' \
                  '&sort=asc' \
                  '&sort_type=created_utc'

fields = ['id', 'title', 'subreddit', 'selftext', 'created_utc', 'retrieved_on', 'num_comments', 'num_crossposts',
          'score']
extract_api = extract_api_url.replace('SUBREDDIT', 'wallstreetbets').replace('START_DATE', str('2021-01-01')) \
    .replace('FIELDS', ','.join(fields))
response = str(requests.get(extract_api).content.decode('utf8'))
list_of_items.extend(json.loads(response)['data'])
