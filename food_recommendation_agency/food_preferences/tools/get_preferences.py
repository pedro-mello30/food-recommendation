from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import os

class GetPreferences(BaseTool):
    """
    Tool for retrieving saved user food preferences
    """
    def run(self):
        """
        Retrieve the user's saved food preferences
        """
        try:
            with open("data/user_preferences.json", "r") as f:
                preferences = json.load(f)
            return json.dumps(preferences, indent=4)
        except FileNotFoundError:
            return "No saved preferences found"

if __name__ == "__main__":
    tool = GetPreferences()
    print(tool.run()) 