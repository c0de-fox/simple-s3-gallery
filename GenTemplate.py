#!/usr/bin/env python3
# GenTemplate.py - Takes PathList files and thumbnails from GenThumb and generates a single page gallery
# Usage: ./GenTemplate.py -p "pathlist file.txt"

from pathlib import Path
import getopt
import random
import sys
import os

baseuri = os.environ.get('BASEURI',"https://s3.wasabisys.com/c0de-photography/")
thumb_path = os.environ.get('THUMBNAILS', "./thumbs")

try:
    opts, args = getopt.getopt(sys.argv[1:],"hp:",["pathlist="])
except getopt.GetoptError:
    print ('GenTemplate.py -p <pathlist file>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print ('GenTemplate.py -p <pathlist file>')
        sys.exit()
    elif opt in ("-p", "--pathlist"):
        pathlist_file = arg # Index file created by GenThumb.py

# Load templates into memory
gallery_template = open('templates/root_gallery.html', 'r').read()
card_template = open('templates/card.html', 'r').read()
crumb_template = """<li class="breadcrumb-item" aria-current="page">{{PATH}}</li>"""

# Get the paths of all JPGs in the thumbnail directory
thumblist = list(Path(thumb_path).rglob("*.[jJ][pP][gG]"))

with open(pathlist_file, 'r') as pathlist:
    with open('index_%s.html' % pathlist_file.strip("pathlist_").strip(".txt"), 'w') as index:
        pathlist = "%s" % pathlist.read()
        pathlist = pathlist.splitlines()
        pathlist.sort()
        thumbrow = ""
        for image in thumblist:
            # Search the pathlist for any lines with a matching filename
            indices = [i for i, s in enumerate(pathlist) if image.name in s]
            if len(indices) > 0:
                imagename = "%s" % image
                the_template = card_template # Don't mutate the source
                the_template = the_template.replace("{{FULLLINK}}", pathlist[indices[0]])
                the_template = the_template.replace("{{TITLE}}", imagename.strip("thumbs/"))
                thumbrow += the_template.replace("{{THUMBNAIL}}", "%s" % image)

        breadcrumbs = pathlist_file.strip("pathlist_").strip(".txt").split(":")
        crumblist = ""
        for crumb in breadcrumbs:
            the_template = crumb_template
            crumblist += the_template.replace("{{PATH}}", crumb)

        index.write(gallery_template.replace("{{THUMBROW}}", thumbrow).replace("{{BREADCRUMBS}}", crumblist))

