import re
def createElement(tag: str,attributes: dict, content: str):
    attributes_str: str = ""
    for attribute in attributes:
        attributes_str += f" {attribute}=\"{attributes[attribute]}\""
    return f"<{tag}{attributes_str}>{content}</{tag}>"

def parser_markdown(content):
    lines = content.split("\n")
    heading_tags = {
        "h1": re.compile(r"^#{1}\s(.*)"),
        "h2": re.compile(r"^#{2}\s(.*)"),
        "h3": re.compile(r"^#{3}\s(.*)"),
        "h4": re.compile(r"^#{4}\s(.*)"),
        "h5": re.compile(r"^#{5}\s(.*)"),
        "h6": re.compile(r"^#{6}\s(.*)"),
    }
    html_source = ""
    for line in lines:
        if heading_tags["h1"].fullmatch(line):
            html_source += createElement("h1",{},heading_tags["h1"].match(line).group(1))
        elif heading_tags["h2"].fullmatch(line):
            html_source += createElement("h2",{},heading_tags["h2"].match(line).group(1))
        elif heading_tags["h3"].fullmatch(line):
            html_source += createElement("h3",{},heading_tags["h3"].match(line).group(1))
        elif heading_tags["h4"].fullmatch(line):
            html_source += createElement("h4",{},heading_tags["h4"].match(line).group(1))
        elif heading_tags["h5"].fullmatch(line):
            html_source += createElement("h5",{},heading_tags["h5"].match(line).group(1))
        elif heading_tags["h6"].fullmatch(line):
            html_source += createElement("h6",{},heading_tags["h6"].match(line).group(1))
        
    return html_source

print(parser_markdown("""## heading1
# heading1"""))