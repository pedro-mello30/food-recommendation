from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import os
from datetime import datetime

class SaveRecommendation(BaseTool):
    """
    Tool for saving restaurant recommendations
    """
    restaurant_name: str = Field(
        ..., 
        description="Name of the recommended restaurant"
    )
    details: dict = Field(
        ..., 
        description="Restaurant details including address, cuisine, price range, etc."
    )

    def run(self):
        """
        Save the restaurant recommendation
        """
        recommendation = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "restaurant_name": self.restaurant_name,
            "details": self.details
        }
        
        os.makedirs("data", exist_ok=True)
        with open("data/recommendations.json", "a") as f:
            f.write(json.dumps(recommendation) + "\n")
        
        return f"Recommendation saved for {self.restaurant_name}"

if __name__ == "__main__":
    tool = SaveRecommendation(
        restaurant_name="Sample Restaurant",
        details={
            "address": "123 Main St",
            "cuisine": "Italian",
            "price_range": "$$",
            "rating": 4.5
        }
    )
    print(tool.run()) 