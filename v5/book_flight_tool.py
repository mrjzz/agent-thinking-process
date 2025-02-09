function_description = [
    {
        "type": "function",
        "function": {
            "name": "book_flight",
            "description": "预定航班",
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
                    },
                    "flight_date": {
                        "type": "string",
                        "description": ""
                    }
                },
                "required": ["loc_origin", "loc_destination", "flight_date"]
            },
        }
    }
]

"""
    tool只负责接收参数，响应为输出
"""
def book_flight(loc_origin, loc_destination, flight_date):
    return f"已预定从{loc_origin}到{loc_destination}的{flight_date}的航班"

class BookFlightTool:
    def get_description(self):
        return function_description

    def call_tool(self, flight_info):
        return book_flight(
            flight_info["loc_origin"],
            flight_info["loc_destination"],
            flight_info["flight_date"]
        )
