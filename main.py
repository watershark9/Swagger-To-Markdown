from Response import Controller
from json import loads, dumps
data = loads(open("swagger.json", "r").read())

x = []

for Key, Value in data["paths"].items():
    path = Key
    req = list(Value.keys())[0]
    try:
        res = next(iter(Value.values()))["responses"]["200"]["content"]["application/json"]["schema"]
        res = dumps(res, indent=4, sort_keys=True)
    except:
        res = None
    x.append(Controller(Key, req, res))
    print(res)
print(path)