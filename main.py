import parser

with open("index.md","r") as f:
    content = f.read()

with open("index.html","w") as f:
    f.write(parser.markdown(content))