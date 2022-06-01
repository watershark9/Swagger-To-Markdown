from json import loads
from Parsers import SwaggerParser, ControllerDictToMarkdown, ControllerDictionary
data = loads(open("swagger.json", "r").read())

Controllers = [SwaggerParser(Key, Value) for Key, Value in data["paths"].items()]
x = ControllerDictionary(Controllers)
y = ControllerDictToMarkdown(x)

with open("swagger.md", "w") as f:
    f.write(y)