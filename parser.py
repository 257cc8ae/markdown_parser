import re


def createElement(tag: str, attributes: dict, content: str):
    attributes_str: str = ""
    for attribute in attributes:
        attributes_str += f" {attribute}=\"{attributes[attribute]}\""
    return f"<{tag}{attributes_str}>{content}</{tag}>"


def markdown(content):
    lines = content.split("\n")
    block_tags = {
        "h1": re.compile(r"^#{1}\s(.*)"),
        "h2": re.compile(r"^#{2}\s(.*)"),
        "h3": re.compile(r"^#{3}\s(.*)"),
        "h4": re.compile(r"^#{4}\s(.*)"),
        "h5": re.compile(r"^#{5}\s(.*)"),
        "h6": re.compile(r"^#{6}\s(.*)"),
        "img_title": re.compile(r"!\[(.*)\]\((.*)\s\"(.*)\"\)"),
        "img": re.compile(r"^!\[(.*)\]\(.*\)"),
        "hr": re.compile(r"^[* -]{3,}"),
        "checkbox": re.compile(r"^-\s\[([\sx])\]\s(.*)"),
    }
    html_source = ""
    for line in lines:
        if block_tags["h1"].fullmatch(line):
            html_source += createElement("h1", {},
                                         block_tags["h1"].match(line).group(1))
        elif block_tags["h2"].fullmatch(line):
            html_source += createElement("h2", {},
                                         block_tags["h2"].match(line).group(1))
        elif block_tags["h3"].fullmatch(line):
            html_source += createElement("h3", {},
                                         block_tags["h3"].match(line).group(1))
        elif block_tags["h4"].fullmatch(line):
            html_source += createElement("h4", {},
                                         block_tags["h4"].match(line).group(1))
        elif block_tags["h5"].fullmatch(line):
            html_source += createElement("h5", {},
                                         block_tags["h5"].match(line).group(1))
        elif block_tags["h6"].fullmatch(line):
            html_source += createElement("h6", {},
                                         block_tags["h6"].match(line).group(1))
        elif block_tags["img_title"].fullmatch(line):
            img_tag = block_tags["img_title"].match(line)
            html_source += createElement("img", {"alt": img_tag.group(
                1), "src": img_tag.group(2), "loading": "lazy", "title": img_tag.group(3)}, "")
        elif block_tags["img"].fullmatch(line):
            img_tag = block_tags["img"].match(line)
            html_source += createElement("img", {"alt": img_tag.group(
                1), "src": img_tag.group(2), "loading": "lazy"}, "")
        elif block_tags["hr"].fullmatch(line):
            html_source += createElement("hr", {}, "")
        elif block_tags["checkbox"].fullmatch(line):
            if block_tags["checkbox"].match(line).group(1) == "x":
                checkbox_attributes = {
                    "type": "checkbox", "disabled": "", "checked": ""
                }
            else:
                checkbox_attributes = {"type": "checkbox", "disabled": ""}
            checkbox: str = createElement("input", checkbox_attributes, "")
            html_source += createElement("li", {}, checkbox + block_tags["checkbox"].match(line).group(2))

    return html_source
