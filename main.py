from json import loads
from Parsers import SwaggerParser, ControllerToMarkdown
data = loads(open("swagger.json", "r").read())

Controllers = [SwaggerParser(Key, Value) for Key, Value in data["paths"].items()]
MarkdownControllers = [ControllerToMarkdown(control) for control in Controllers]

with open("swagger.md", "w") as sw:
    sw.write("\n".join(MarkdownControllers).replace("\n\n","\n"))