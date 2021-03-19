import random
import twitter

twitter_keyset = [
    {
        "scheduled_every": "60",
        "tweet_mode": "extended",
        "api_key": "ABC",
        "api_secret_key": "DEF",
        "bearer_token": "GHI",
        "acess_token": "JKL",
        "acess_token_secret": "MNO"
    },
    {
        "scheduled_every": "60",
        "tweet_mode": "extended",
        "api_key": "PQR",
        "api_secret_key": "STU",
        "bearer_token": "VUX",
        "acess_token": "YZA",
        "acess_token_secret": "BCD"
    }
]


def search(keyword, since_id, tweeter_keys):
    # keyword[0] contains list of words to include
    query = 'q=' + '%22' + keyword[0].replace(' ', '%20') + '%22'
    # keyword[1] contains list of words to exclude
    if keyword[1] != '':
        for x in keyword[1].split(';'):
            query += '%20-' + x
    print(query)
    return _create_twitter_api(tweeter_keys).GetSearch(raw_query=query, lang='en', count=5, return_json=True,
                                                       since_id=since_id)


def _create_twitter_api(tweeter_keys):
    return twitter.Api(
        consumer_key=tweeter_keys['api_key'],
        consumer_secret=tweeter_keys['api_secret_key'],
        access_token_key=tweeter_keys['acess_token'],
        access_token_secret=tweeter_keys['acess_token_secret'],
        tweet_mode='extended'  # tweeter_keys['tweet_mode'],
    )


if __name__ == '__main__':
    # rotate keys for twitter
    tweeter_keys = random.choice(twitter_keyset)
    # fetch tweets for apple inc, exclude tweets with fruit or jam or plant.
    data = search(['apple', 'fruit jam plant'], 1345725780316197864, tweeter_keys)
    print(data)
