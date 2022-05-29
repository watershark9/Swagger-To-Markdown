class Controller:
    def __init__(self, path, req, res = None, params: list = None) -> None:
        self.Path: str = path
        self.Description: str = ""
        self.Request: str = req.upper()
        self.Response: str = res
        self.Parameters: list = params or None