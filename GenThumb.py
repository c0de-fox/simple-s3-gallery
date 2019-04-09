#!/usr/bin/env python3
# GenThumb.py - Part of the simple s3 gallery
# Usage: ./GenThumb.py

from pathlib import Path
from PIL import Image
import logging
import _thread
import time

logging.basicConfig(filename='GenThumb.log', level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info("---------------")

baseuri = "https://s3.wasabisys.com/c0de-photography/"
s3_path = "/mnt/photos/"
browse_path = "EOS M100/"
thumb_path = "./thumbs"
thumbsize = (250, 250)


logging.info("Getting Paths (Can take time on large directories)")
filelist = list(Path(s3_path + browse_path).rglob("*.[jJ][pP][gG]"))
thumblist = list(Path(thumb_path).rglob("*.[jJ][pP][gG]"))

def gen_thumb(image):
    imagepath = "%s" % image.parent
    imagepath = imagepath.strip(s3_path)
    pathlist.write(baseuri + imagepath + image.name)
    thumbname = "%s/%s:%s" % (thumb_path, imagepath, image.name)

    if image.name in "%s" % thumblist:
        logging.debug("Skipping %s" % image)
    else:
        logging.info("Generating thumbnail for New Image: %s" % (image))

        img = Image.open(image)
        img.thumbnail(thumbsize)
        img.save(thumbname)

        logging.info("Saved Thumbnail as %s" % thumbname)

with open('pathlist.txt', 'w') as pathlist:
    for image in filelist:
        try:
            _thread.start_new_thread(gen_thumb, (image,))
            time.sleep(0.15)
        except:
            logging.error("unable to start thread")

logging.info("Wait for all threads to save")

while(1):
    pass

