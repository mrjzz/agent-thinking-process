function_description = [
    {
        "type": "function",
        "function": {
            "name": "get_flight_info",
            "description": "获取航班的起始机场地点",
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
    return f"从{loc_origin}到{loc_destination}最早的航班是早上七点"

class GetFlightInfoTool:
    def get_description(self):
        return function_description

    def call_tool(self, flight_info):
        return get_flight_info(flight_info["loc_origin"], flight_info["loc_destination"])
