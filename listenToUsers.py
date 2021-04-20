class StdOutListener(StreamListener):

    def on_status(self, status):
        if status.user.id_str != '<user_id>':
            req.post("https://api.telegram.org/bot-code/"
                 "sendMessage?chat_id=-XXXXXX&text=" + status.text)
            print(status.text)
            return

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    access_token = "your token"
    access_secret = "your token"
    consumer_key = "your token"
    consumer_secret = "your token"
    # This handles Twitter authentication and connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)
    st = stream.filter(follow=['998965508765552640', '1276977568466505728', '1170831448082984960', '101730133'])
