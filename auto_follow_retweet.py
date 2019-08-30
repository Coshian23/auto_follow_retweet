import tweepy

def lambda_handler(event, context):

    # doc twitter account
    CONSUMER_KEY = "AbZQOQfJhhepEf29CvqGiuglS"
    CONSUMER_SECRET = "VqyXmtDlaZnKy9WkHDtq0Raioe71fH317Iwi4isjg4SAGN5zqD"
    ACCESS_TOKEN = "1166294649364860928-8qvnfDAF0uKkrpHEyKNIDUwj1NgEaq"
    ACCESS_SECRET = "O87jotf4uYXrZRt6FdQsNA4bVA8U9b5IFv2LfvuKXR2Ho"

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    #search_results = api.search(q="フォロー RT 応募 OR @9999 -filter:retweets -filter:replies filter:verified", count=10)
    search_results = api.search(q="フォロー RT 応募 filter:verified")

    for result in search_results:
        tweet_id = result.id
        user_id = result.user._json['id']
        print(tweet_id)
        try:
            #api.create_favorite(tweet_id)
            api.create_friendship(user_id)
            api.retweet(tweet_id)
            print(user_id)
        except Exception as e:
            print(e)

lambda_handler("", "")