from Response import Controller

def SwaggerParser(Key, Value) -> Controller:
    from json import dumps

    # path = Key
    request = list(Value.keys())[0]
    response = None
    parameters = []
    description = ""
    group = ""
    
    try:
        res = next(iter(Value.values()))["responses"]["200"]["content"]["application/json"]["schema"]
        response = dumps(res, indent=4, sort_keys=True)
    except:
        res = None
    try:
        params = next(iter(Value.values()))["parameters"]
        for par in params:
            val = None
            try:
                val = par["schema"]["format"]
            except:
                val = par["schema"]["type"]
            parameters.append((par["name"],val))
    except:
        par = None
    description = next(iter(Value.values()))["summary"]
    group = next(iter(Value.values()))["tags"][0]

    return Controller(Key, request, response, parameters, description, group)

def GetControllerList(lstCtrl: list) -> list:
    list = set()
    for controller in lstCtrl:
        if controller.Controller not in list:
            list.add(controller.Controller)
    return list

def ControllerDictionary(lstCtrl: list) -> dict:
    dictx = {}
    for key in GetControllerList(lstCtrl):
        dictx[key] = []
    for controller in lstCtrl:
        dictx[controller.Controller].append(controller)
    return dictx

def ControllerDictToMarkdown(lstCtrl: dict) -> str:
    values = ""
    for Key, Values in lstCtrl.items():
        Section = f"## {Key}\n"
        Content = ""
        if isinstance(Values, list):
            for value in Values:
                Content += value.ToMarkdown() + "\n"
        else:
            Content += Values + "\n"
        values += Section + Content
    return values