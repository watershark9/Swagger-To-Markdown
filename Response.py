class Controller:
    def __init__(self, path, req, res = None, params: list = None, desc = "") -> None:
        self.Path: str = path
        self.Description: str = desc
        self.Request: str = req.upper()
        self.Response: str = res
        self.Parameters: list = params or None