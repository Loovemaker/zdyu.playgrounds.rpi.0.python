from urllib import request, parse


def v1(token: str):

    def send(message: str):
        data = parse.urlencode({'text': message}).encode()
        req = request.Request(
            "https://api.chanify.net/v1/sender/{}"
                .format(token),
            data=data
        )
        request.urlopen(req)
        print("Sent: {}".format(message))

    return send
