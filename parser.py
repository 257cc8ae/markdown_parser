import re
def createElement(tag: str,attributes: dict, content: str):
    attributes_str: str = ""
    for attribute in attributes:
        attributes_str += f" {attribute}=\"{attributes[attribute]}\""
    return f"<{tag}{attributes_str}>{content}</{tag}>"

def parser_markdown(content):
    lines = content.split(r"\n")
    h1_tag = re.compile(r"^#{1}\s(.*)")
    html_source = ""
    for line in lines:
        if h1_tag.fullmatch(line):
            html_source += createElement("h1",{},h1_tag.match(line).group(1))
    return html_source

print(parser_markdown("""# heading1"""))