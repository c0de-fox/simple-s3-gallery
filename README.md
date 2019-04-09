# Simple S3 Gallery

This is a very simple web gallery that depends on all your files being hosted away from this server (can be static!). Basically it expects your storage be mounted and readable by your current user.

After scanning through your storage, it will generate thumbnails locally and a list of all the public URLs. This list is fed into the layout generator to create the gallery site.

Upcoming: Systemd timer to scan this daily
