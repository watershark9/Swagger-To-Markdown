from Response import Controller

def SwaggerParser(Key, Value) -> Controller:
    from json import dumps

    path = Key
    request = list(Value.keys())[0]
    response = None
    parameters = []
    
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
        
    return Controller(Key, request, response, parameters)

def ControllerToMarkdown(ctrl: Controller) -> str:
    Head = f"## `{ctrl.Path}` - **{ctrl.Request}**\n"
    Description = ""
    #Description = "{replacethisfornow}"

    Parameters = ""
    if ctrl.Parameters is not None:
        Parameters = "### Parameters\n| Name | Type |\n|---|---|\n"
        for Param in ctrl.Parameters:
            Parameters += f"| {Param[0]} | {Param[1]} |\n"

    Result = ""
    if ctrl.Response is not None:
        Result = f"### Result\n```json\n{ctrl.Response}\n```"

    return f"""{Head}\n{Description}\n{Parameters}\n{Result}"""