#!/usr/bin/python
import webbrowser
import sys
import os
import itertools

with open(os.path.abspath(sys.argv[1])) as u:
	if len(sys.argv)<=3:
		url = u.readlines()[int(sys.argv[2])-int(1)]
		webbrowser.get('firefox').open(url)
	else:
 	    for url in itertools.islice(u,int(sys.argv[2])-int(1),int(sys.argv[3])):
   	  		webbrowser.get('firefox').open(url)

        
