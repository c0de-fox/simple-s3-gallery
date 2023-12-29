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
                "src": "./templates/static/bootstrap.bundle.min.js",
            },
            "theme": {"src": "./templates/static/color-modes.js", "place_in_head": True},
        },
        "css": {
            "bootstrap": {"src": "./templates/static/bootstrap.min.css"},
            "theme": {"src": "./templates/static/gallery.css"},
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
            {"text": "something"},
            {"theme": "danger", "text": "something dangerous"},
            {"href": "3", "theme": "warning", "icon": "exclamation-diamond-fill"},
            {
                "href": "3",
                "theme": "warning",
                "icon": "exclamation-diamond-fill",
                "text": "some text",
            },
        ],
    },
    "gallery": {
        "max_reactions_per_card": 9,
    },
    "gallery_items": [
        {
            "src": "https://files.c0defox.es/Pictures/arctic-fox.jpg",
            "description": "An arctic fox :3",
            "title": "fox",
            "reactions": {
                "0-circle": 1,
                "1-circle": 2,
                "2-circle": 3,
                "3-circle": 4,
                "4-circle": 5,
                "5-circle": 6,
                "6-circle": 7,
                "7-circle": 8,
                "8-circle": 9,
                "9-circle": 10,
                "0-circle-fill": 11,
                "1-circle-fill": 12,
                "2-circle-fill": 13,
                "3-circle-fill": 14,
                "4-circle-fill": 15,
                "5-circle-fill": 16,
                "6-circle-fill": 17,
                "7-circle-fill": 18,
                "8-circle-fill": 19,
                "9-circle-fill": 20,
            },
        },
        {
            "src": "https://files.c0defox.es/Pictures/20150825_114759.jpg",
            "description": "The inside of a Data Center",
            "title": "Data Center",
            "reactions": {"heart-fill": 1024, "bag-x-fill": 50},
        },
        {
            "src": "https://secure.gravatar.com/avatar/1e346a54257cf0a9932fcfc1e61c015d?s=200",
            "description": "",
            "title": "",
        },
        {
            "src": "https://c0defox.es/paw-tail.svg",
            "alt_text": "a fox tail next to a paw print",
            "title": ""
        }
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
