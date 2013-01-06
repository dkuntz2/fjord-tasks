#!/usr/bin/env python

from subprocess import call
from sys import argv
from datetime import datetime

now = datetime.now()


# set the message
gitmessage = now.strftime("[%d %B %Y %H:%M] ")
gitmessage += argv[1] if len(argv) > 1 else "Generic Update"

print(gitmessage)

# make sure there are no remote changes
call(["git", "pull"])

# update the git repo
call(["git", "add", "."])
call(["git", "commit", "-m", gitmessage])
call(["git", "push"])

# update the site
call(["fjord", "gen", "-f", "./", "_site"])

# rsync the site
call([
    "rsync",
    "-rupaz",
    "_site/",
    "don@kuntz.co:~/sites/dkuntz2.com"
])

