#!/usr/bin/python3

"""
test template rendering
python3 test.py | tee test.html
python3 -m http.server
"""

from jinja2 import Environment, FileSystemLoader, select_autoescape

template_vars = {
    "charset": "utf-8",
    "language": "en",
    "css_theme_name": "auto",
    "canonical_url": "http://example.com",
    "page_title": "This is a title",
    "theme": "dark",
    "text_theme": "white",
    "static": {
        "scripts": {
            "bootstrap": {
                "src": "./templates/example/bootstrap.bundle.min.js",
            },
            "theme": {"src": "./templates/example/color-modes.js"},
        },
        "css": {
            "bootstrap": {"src": "./templates/example/bootstrap.min.css"},
            "theme": {"src": "./templates/example/gallery.css"},
            "icons": {
                "src": "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.2/font/bootstrap-icons.min.css"
            },
        },
    },
    "meta_list": [
        {"name": "description", "content": "This is a description"},
        {"name": "generator", "content": "simple-s3-gallery v.2023.12"},
        {"name": "author", "content": "Code Fox"},
        {"name": "theme-color", "content": "#712cf9"},
    ],
    "left_header": "About the gallery",
    "left_text": "This is an example gallery that is generated via a template",
    "right_header": "Contact",
    "link_list": [
        {"href": "https://c0defox.es", "text": "Fox :3"},
        {"href": "https://furry.engineer/c0de", "text": "Mastodon", "icon": "mastodon"},
    ],
    "footer": {
        "main_line": "Copyright 2024 Code Fox",
        "extra_lines": ["This is another line", "This is yet another line"],
    },
    "call_to_action": {
        "active": True,
        "header": "This is a call to action",
        "lead_text": "Some interesting text for the user",
        "buttons": [
            {"href": "1"},
            {"href": "2", "theme": "danger"},
            {"href": "3", "theme": "warning", "icon": "exclamation-diamond-fill"},
            {
                "href": "3",
                "theme": "warning",
                "icon": "exclamation-diamond-fill",
                "text": "some text",
            },
        ],
    },
    "gallery_items": [
        {
            "src": "https://files.c0defox.es/Pictures/arctic-fox.jpg",
            "description": "An arctic fox :3",
            "title": "fox",
            "reactions": ["heart-fill", "backpack4", "balloon-fill", "bag-x-fill"],
        },
        {
            "src": "https://files.c0defox.es/Pictures/arctic-fox.jpg",
            "description": "An arctic fox :3",
            "title": "fox",
            "reactions": [],
        },
        {
            "src": "https://files.c0defox.es/Pictures/arctic-fox.jpg",
            "description": "An arctic fox :3",
            "title": "fox",
        },
    ],
}


def main():
    """main method"""

    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("base.html")
    print(template.render(**template_vars))


if __name__ == "__main__":
    main()
