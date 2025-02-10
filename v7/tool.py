from abc import ABC, abstractmethod

class Tool(object):
    def __init__(self, tools):
        self.tools = tools


class BaseTool(ABC):
    @abstractmethod
    def __init__(self, func_name, description, parameters):
        pass

    @abstractmethod
    def callable_func(self):
        pass

    @abstractmethod
    def call_tool(self, args):
        pass