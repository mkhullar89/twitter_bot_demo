import tweepy
import time
print('This is My Twitter Bot')

CONSUMER_KEY='7fGZwQJe7nl0IkvrJ6sj3QQyE'
CONSUMER_SECRET='IyCtQC03Px317X3VqhyjmQqrepYz6W3Ma0qhiU2Xw5RInDRSt6'
ACCESS_KEY='2816647934-xVoRFpvMt5lD6rVC4H7GLUSE2Qg6ZfyqvWFKDxg'
ACCESS_SECRET='JWdtbfNJK4CQ3PgBH5RgshjYn908ZRoA8a2FP4DPv6PPB'
auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)
mentions=api.mentions_timeline();

FILE_NAME='last_seen_id.txt'
def retrieve_last_seen_id(file_name):
    f_read=open(file_name,'r')
    last_seen_id=int(f_read.read().strip())
    f_read.close();
    return last_seen_id
def store_last_seen_id(last_seen_id,file_name):
    f_write=open(file_name,'w')
    f_write.write(str(last_seen_id));
    f_write.close();
    return
def reply_to_tweet():
    print("Retriving and Replying of Tweet")
    last_seen_id=retrieve_last_seen_id(FILE_NAME)
    mentions=api.mentions_timeline(last_seen_id,tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id)+ '-' + mention.full_text)
        last_seen_id=mention.id
        store_last_seen_id(last_seen_id,FILE_NAME)
        if '#askmanav' in mention.full_text.lower():
            print("found #askmanav");
            print("Replying Back");
            api.update_status('Hello'+'@' +mention.user.screen_name+ 'I have heard your query and will try to put in upcoming video',mention.id)
while True:
    reply_to_tweet();
    time.sleep(15)

