#!/usr/bin/env python3
# GenThumb.py - Part of the simple s3 gallery
# Usage: ./GenThumb.py

from pathlib import Path
import getopt
import sys
import os

# Set these to override
baseuri = os.environ.get('BASEURI',"https://s3.wasabisys.com/c0de-photography/")
thumb_path = os.environ.get('THUMBNAILS', "./thumbs")

# Load templates into memory
gallery_template = open('templates/root_gallery.html', 'r').read()
card_template = open('templates/card.html', 'r').read()

# Get all the index files in local directory
indexlist = list(Path(".").rglob("index_*.html"))

with open('gallery.html', 'w') as gallery:
    thumbrow = ""
    for index in indexlist:
        the_template = card_template # Don't mutate the source
        # basic string replacements
        the_template = the_template.replace("{{FULLLINK}}", index.name)
        the_template = the_template.replace("{{TITLE}}", index.name.strip("index_").strip(".html").replace(":", "/"))
        thumbrow += the_template.replace("{{THUMBNAIL}}", "thumbs/folder.png")
    gallery.write(gallery_template.replace("{{THUMBROW}}", thumbrow))

