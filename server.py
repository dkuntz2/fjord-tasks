#!/usr/bin/env python

from subprocess import call
from os import chdir
from threading import Thread
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


class CompileSCSS(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        call([
            "sass",
            "--watch",
            "_assets/_scss:_assets/css"
        ])


class SimpleServer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.httpd = None

    def run(self):
        chdir("_site")
        self.httpd = TCPServer(('', 8000), SimpleHTTPRequestHandler)
        self.httpd.serve_forever()

    def shutdown(self):
        self.httpd.shutdown()


class MyntWatcher(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        call(["mynt", "watch", "-f", "--base-url=http://127.0.0.1:8000/", "./", "_site"])


try:
    threads = []

    scss = CompileSCSS()
    threads.append(scss)
    scss.start()

    myntwatch = MyntWatcher()
    threads.append(myntwatch)
    myntwatch.start()

    serv = SimpleServer()
    threads.append(serv)
    serv.start()

    while True:
        pass

except(KeyboardInterrupt, SystemExit):
    print("Kill signal received! Killing threads...")
    for t in threads:
        t.kill_received = True
    serv.shutdown()
