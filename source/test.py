import re

with open("../AUTHORS", "r") as f:
    author = list(re.findall(r"^\*\s(.*)", f.read(), re.MULTILINE))

print(author)
