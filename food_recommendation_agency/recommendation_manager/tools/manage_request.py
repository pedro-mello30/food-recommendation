from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import os
from datetime import datetime

class ManageRequest(BaseTool):
    """
    Tool for managing food recommendation requests and coordinating with other agents.
    """
    request_type: str = Field(
        ..., 
        description="Type of request (initial, preferences, recommendation)"
    )
    user_input: str = Field(
        ..., 
        description="User's input or request details"
    )

    def run(self):
        """
        Process the request and determine next steps in the recommendation workflow
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create request log
        request_data = {
            "timestamp": timestamp,
            "type": self.request_type,
            "input": self.user_input
        }
        
        # Save request to a JSON file
        os.makedirs("data", exist_ok=True)
        with open("data/request_log.json", "a") as f:
            f.write(json.dumps(request_data) + "\n")
        
        return f"Request processed: {self.request_type} at {timestamp}"

if __name__ == "__main__":
    tool = ManageRequest(request_type="initial", user_input="Looking for dinner recommendations")
    print(tool.run()) 