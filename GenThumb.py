#!/usr/bin/env python3
# GenThumb.py - Takes a directory listing and generates thumbnails for all JPGs, as well as creates a PathList.txt file
# Usage: ./GenThumb.py -b "S3MOUNT(implicit)/path/to/browse"

from pathlib import Path
from PIL import Image
import logging
import _thread
import time
import getopt
import sys
import os

logging.basicConfig(filename='GenThumb.log', level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info("---------------")

baseuri = os.environ.get('BASEURI',"https://s3.wasabisys.com/c0de-photography/")
s3_path = os.environ.get('S3MOUNT', "/mnt/photos/")
thumb_path = os.environ.get('THUMBNAILS', "./thumbs")
thumbsize = (250, 250)

try:
    opts, args = getopt.getopt(sys.argv[1:],"hb:",["browse="])
except getopt.GetoptError:
    print ('GenThumb.py -b <browse path>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print ('GenThumb.py -b <browse path>')
        sys.exit()
    elif opt in ("-b", "--browse"):
        browse_path = arg

logging.info("Getting Paths (Can take time on large directories)")
filelist = list(Path(s3_path + browse_path).rglob("*.[jJ][pP][gG]"))
thumblist = list(Path(thumb_path).rglob("*.[jJ][pP][gG]"))

def gen_thumb(image, imagepath):
    Path(thumb_path + '/' + imagepath).mkdir(mode=0o755, parents=True, exist_ok=True) # Generate the path if it doesn't already exist
    thumbname = "%s/%s/%s" % (thumb_path, imagepath, image.name)

    if image.name in "%s" % thumblist:
        logging.debug("Skipping %s" % image)
    else:
        logging.info("Generating thumbnail for New Image: %s" % (image))

        img = Image.open(image)
        img.thumbnail(thumbsize)
        img.save(thumbname)

        logging.info("Saved Thumbnail as %s" % thumbname)

logging.debug("Creating pathlist file as: pathlist_%s.txt" % browse_path.replace('/', ':'))
with open('pathlist_%s.txt' % browse_path.replace('/', ':'), 'w') as pathlist:
    for image in filelist:
        imagepath = "%s" % image.parent
        imagepath = imagepath.strip(s3_path)
        # The pathlist file is used by GenTemplate.py to generate a specific gallery for a specific directory and its children
        pathlist.write(baseuri + imagepath + '/' + image.name + '\n')
        try:
            # WARNING: Each file found will become a thread! Be sure your computer can handle the load
            _thread.start_new_thread(gen_thumb, (image, imagepath,))
            time.sleep(0.15)
        except:
            logging.error("unable to start thread")

logging.info("Wait for all threads to save")

while(1):
    pass

