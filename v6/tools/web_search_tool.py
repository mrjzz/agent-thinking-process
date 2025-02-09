

from v6.tool import BaseTool
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebSearchTool(BaseTool):
    def __init__(self, description, parameters):
        self.func_name = "callable_func"
        self.description = description
        self.parameters = parameters
        self.options = Options()
        self.options.add_argument("--headless")  # 无头模式
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=self.options)

    def generate_description(self):
        return [
            {
                "type": "function",
                "function": {
                    "name": self.func_name,
                    "description": self.description,
                    "parameters": {
                        "type": "object",
                        "properties": {
                            param: {
                                "type": "string",
                                "description": ""
                            } for param in self.parameters
                        },
                        "required": self.parameters
                    }
                }
            }
        ]

    def callable_func(self, url):
        try:
            self.driver.get(url)
            # 显式等待直到目标元素加载完成
            WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.channel-feed-list"))
            )
            return self.driver.page_source
        except Exception as e:
            print(f"爬取失败: {str(e)}")
            return ""
        finally:
            self.driver.quit()

    def call_tool(self, args):
        return self.callable_func(
            *(args[param] for param in self.parameters)
        )
