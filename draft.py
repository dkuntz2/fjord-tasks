#!/usr/bin/env python

import os
import re
#from exceptions import Exception
from sys import argv

if len(argv) != 2:
	raise Exception("There is no title argument")

title = argv[1]

dirn = "_drafts/"
if not os.path.exists(dirn):
    os.makedirs(dirn)

filename = dirn + re.sub(r'\W+', '-', title.lower()) + ".md"

filecont =  "---\ntitle: \"" + title + "\""
filecont += "\nlayout: post.html"
filecont += "\ntags: []\n---\n\n"

writer = open(filename, "w")
writer.write(filecont)

