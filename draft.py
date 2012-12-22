from os import path,makedirs
from re import sub
from system import argv
from exception import Exception

if len(argv) != 2:
    raise Exception("There is no title argument")

title = argv[1]

dirn = "_drafts/"
if not path.exists(dirn):
    makedirs(dirn)

filename = dirn + sub(r'\W+', '-', title.lower() + ".md")

filecont =  "---\ntitle: \"" + title + "\""
filecont += "\nlayout: post.html"
filecont += "\ntags: []\n---\n\n"

writer = open(filename, "w")
writer.write(filecont)
