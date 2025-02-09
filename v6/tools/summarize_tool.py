

from v6.tool import BaseTool

class SummarizeTool(BaseTool):
    def __init__(self, description, parameters):
        self.func_name = "callable_func"
        self.description = description
        self.parameters = parameters

    def generate_description(self):
        return None

    def callable_func(self):
        pass

    def call_tool(self, args):
        return self.callable_func(
            *(args[param] for param in self.parameters)
        )
