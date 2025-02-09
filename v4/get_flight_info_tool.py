function_description = [
    {
        "type": "function",
        "function": {
            "name": "get_flight_info",
            "description": "get flight info between two airports",
            "parameters": {
                "type": "object",
                "properties": {
                    "loc_origin": {
                        "type": "string",
                        "description": ""
                    },
                    "loc_destination": {
                        "type": "string",
                        "description": ""
                    }
                },
                "required": ["loc_origin", "loc_destination"]
            },
        }

    }
]

"""
    tool只负责接收参数，响应为输出
"""
def get_flight_info(loc_origin, loc_destination):
    print(f"出发地是{loc_origin}")
    print(f"终点是{loc_destination}")
    return "早上七点"

class GetFlightInfoTool:
    def get_description(self):
        return [
            {
                "type": "function",
                "function": {
                    "name": "get_flight_info",
                    "description": "get flight info between two airports",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "loc_origin": {
                                "type": "string",
                                "description": ""
                            },
                            "loc_destination": {
                                "type": "string",
                                "description": ""
                            }
                        },
                        "required": ["loc_origin", "loc_destination"]
                    },
                }

            }
        ]

    def call_tool(self, flight_info):
        return get_flight_info(flight_info["loc_origin"], flight_info["loc_destination"])
    def __init__(self):
        self.funcs = {
            "get_flight_info": get_flight_info
        }
    def __getitem__(self, item):
        return self.funcs[item]
