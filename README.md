# Simple S3 Gallery

This is a very simple web gallery that depends on all your files being hosted away from this server (can be static!). Basically it expects your storage be mounted and readable by your current user.

After scanning through your storage, it will generate thumbnails locally and a list of all the public URLs. This list is fed into the layout generator to create the gallery site.

Upcoming: Systemd timer to scan this daily


## Usage:

1. Configure your S3 bucket to have public read permissions
1. Have your S3 bucket mounted and readable (I used s3fs-fuse)
1. `export BASEURI="https://[your s3 bucket URL here]"`
1. `export S3MOUNT=/path/to/your/bucket/mount`
1. `export THUMBNAILS=/path/to/stored/thumbnails`
1. Generate thumbnails - `./GenThumb.py -b "Specific/Folder/Inside/S3MOUNT"` -- WARNING - This will create a thread for every image found, ensure your computer can handle the load
1. Generate an index/single page gallery - `./GenTemplate.py -p [Pathlist file from GenThumb]`
1. You now have a fully static gallery! Install the index.html and thumbs directory on your webserver
