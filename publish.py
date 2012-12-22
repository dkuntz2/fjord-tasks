#!/usr/bin/env python

from datetime import datetime
from subprocess import call
from os import path, makedirs, chdir
from shutil import move

from sys import argv

# if there isn't a draft argument
if len(argv) != 2:
    raise Exception("No file specified")

draft = argv[1]

if path.isfile(draft):
    now = datetime.now()
    pubd = "source/_posts/" + now.strftime("%Y/%m/%d/")

	if not path.exists(pubd):
		makedirs(pubd)
    
    pub = pubd + now.strftime("%Y-%m-%d-%H-%M-")
	# I *could* hard code in a size (in this case 8), but what if someone
	# wants to use this, but has a different directory structure? What then?
	pub += title[len("_drafts/"):]

	move(draft, pub)

else:
    print(str(draft) + "could not be found")

