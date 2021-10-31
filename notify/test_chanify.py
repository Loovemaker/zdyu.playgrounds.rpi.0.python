from unittest import TestCase
import time

from notify import chanify

token = "CMSo048GEiJBQ1lETjU3SEQ0NjJUWUZZWVUzREVGTVFCQVRGSzNRSUFRIggIAhoEdGVzdA.6ZGBdcdg9jjEbNdJ9uECbfmyiyjIVAyhHFldV0t6-V4"

actions = {
    "hello": lambda: messages_at_time("Hello, world!")
}

messages_at_time = lambda string: "{} at {}".format(string, time.asctime())


class Test(TestCase):

    def test_v1(self):
        send = chanify.v1(token)
        hello = actions["hello"]()
        send(hello)
