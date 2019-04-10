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

template = """
<html>
    <head>
        <title>Simple S3 Gallery</title>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="David Todd" />
        <link rel="icon" type="image/png" href="https://secure.gravatar.com/avatar/1e346a54257cf0a9932fcfc1e61c015d" />

        <!-- Bootstrap core CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <style>
            .bg-dark {
                background-color: #343a40cc !important;
            }

            nav.bcrumb {
                margin-left: 1rem;
                margin-top: 0.5rem;
            }

            .jumbotron {
                padding-top: 3rem;
                padding-bottom: 3rem;
                margin-bottom: 0;
                background-color: #fff;
            }
            @media (min-width: 768px) {
                .jumbotron {
                    padding-top: 6rem;
                    padding-bottom: 6rem;
                }
            }

            .jumbotron p:last-child {
                margin-bottom: 0;
            }

            .jumbotron-heading {
                font-weight: 300;
            }

            .jumbotron .container {
                max-width: 40rem;
            }

            .card-header {
                text-align: center;
                padding: 0.25rem 0rem;
            }

            footer {
                padding-top: 3rem;
                padding-bottom: 3rem;
            }

            footer p {
                margin-bottom: .25rem;
            }
        </style>
    </head>
    <body>
        <header>
            <div class="collapse bg-dark" id="navbarHeader">
                <div class="container">
                    <div class="row">
                        <div class="col-sm-8 col-md-7 py-4">
                            <h4 class="text-white">About</h4>
                            <p class="text-white">This is a small gallery to represent images that I have taken over the past few years. Most of these are unsorted and unedited, and thus a lot are blurry or have lighting issues. I have taken, and thereby own all photos on this site.</p>
                        </div>
                        <div class="col-sm-4 offset-md-1 py-4">
                            <h4 class="text-white">Contact</h4>
                            <ul class="list-unstyled">
                                <li><a href="https://c0defox.es" class="text-white">My contact site</a></li>
                                <li><a href="https://t.me/c0defox" class="text-white">Hit me up on Telegram</a></li>
                                <li><a href="c0de#0689" class="text-white">My Discord is c0de#0689</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="navbar navbar-dark bg-dark shadow-sm">
                <div class="container d-flex justify-content-between">
                <span class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="mr-2" viewBox="0 0 24 24" focusable="false"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
                    <strong>Simple S3 Gallery</strong>
                    <nav class="text-dark bcrumb" aria-label="breadcrumb">
                        <ol class="breadcrumb">
                            {{BREADCRUMBS}}
                        </ol>
                    </nav>
                </span>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                </div>
            </div>
        </header>

        <main role="main">

            <!-- Optional for creating a notification -->
            <!--
            <section class="jumbotron text-center">
                <div class="container">
                    <h1 class="jumbotron-heading">Album example</h1>
                    <p class="lead text-muted">Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don’t simply skip over it entirely.</p>
                    <p>
                        <a href="#" class="btn btn-primary my-2">Main call to action</a>
                        <a href="#" class="btn btn-secondary my-2">Secondary action</a>
                    </p>
                </div>
            </section>
            -->

            <div class="album py-3 bg-dark">
                <div class="container">
                    <div class="row">
                        {{THUMBROW}}
                    </div>
                </div>
            </div>
        </main>

        <footer class="text-muted">
            <div class="container">
                <p class="float-right"><a href="#">Back to top</a></p>
                <p>Simple S3 Gallery &copy; 2019 <a href="https://c0defox.es">David Todd</a> - All photos are &copy; <a href="https://dtodd.us">David Todd</a></p>
            </div>
        </footer>

        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
</html>
"""

template2 = """
<div class="col-md-3">
    <a href="{{FULLLINK}}" target="{{FULLLINK}}">
        <div class="card mb-3 bg-dark text-white rounded">
            <div class="card-header">{{TITLE}}</div>
            <img class=card-img" width="100%" height="100%" src="{{THUMBNAIL}}" />
        </div>
    </a>
</div>
"""

crumb_template = """<li class="breadcrumb-item" aria-current="page">{{PATH}}</li>"""

thumblist = list(Path(thumb_path).rglob("*.[jJ][pP][gG]"))

with open(pathlist_file, 'r') as pathlist:
    with open('index_%s.html' % pathlist_file.strip("pathlist_").strip(".txt"), 'w') as index:
        pathlist = "%s" % pathlist.read()
        pathlist = pathlist.splitlines()
        pathlist.sort()
        thumbrow = ""
        for image in thumblist:
            indices = [i for i, s in enumerate(pathlist) if image.name in s]
            if len(indices) > 0:
                imagename = "%s" % image
                the_template = template2
                the_template = the_template.replace("{{FULLLINK}}", pathlist[indices[0]])
                the_template = the_template.replace("{{TITLE}}", imagename.strip("thumbs/"))
                thumbrow += the_template.replace("{{THUMBNAIL}}", "%s" % image)

        breadcrumbs = pathlist_file.strip("pathlist_").strip(".txt").split(":")
        crumblist = ""
        for crumb in breadcrumbs:
            the_template = crumb_template
            crumblist += the_template.replace("{{PATH}}", crumb)

        index.write(template.replace("{{THUMBROW}}", thumbrow).replace("{{BREADCRUMBS}}", crumblist))

