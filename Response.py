class Controller:
    def __init__(self, path, req, res = None, params: list = None, desc = "", group: str = None) -> None:
        self.Path: str = path
        self.Description: str = desc
        self.Request: str = req.upper()
        self.Response: str = res
        self.Parameters: list = params or None
        self.Controller: str = group

    def ToMarkdown(self) -> str:
        Head = f"### `{self.Path}` - **{self.Request}**"
        Description = self.Description

        Parameters = ""
        if self.Parameters is not None:
            Parameters = "#### Parameters\n| Name | Type |\n|---|---|\n"
            for Param in self.Parameters:
                Parameters += f"| {Param[0]} | {Param[1]} |\n"

        Result = ""
        # if self.Response is not None:
        #     Result = f"### Result\n```json\n{self.Response}\n```"

        return f"{Head}\n{Description}\n{Parameters}\n{Result}"