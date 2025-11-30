"""Resource Agent
Simple wrapper for the Google Search tool (replace with real search tool).
"""
from tools.google_search_tool import GoogleSearchTool




class ResourceAgent:
def __init__(self):
self.search_tool = GoogleSearchTool()


def search(self, query: str):
# returns list of {title, url, snippet}
return self.search_tool.search(query)
