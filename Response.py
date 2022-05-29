class Controller:
    def __init__(self, path, req, res) -> None:
        self.Path = path
        self.Request = req
        self.Response = res