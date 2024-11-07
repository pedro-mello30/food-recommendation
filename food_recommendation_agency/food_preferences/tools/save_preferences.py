from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import os

class SavePreferences(BaseTool):
    """
    Tool for saving user food preferences and dietary restrictions
    """
    cuisine_type: str = Field(
        ..., 
        description="Preferred cuisine type(s)"
    )
    dietary_restrictions: str = Field(
        ..., 
        description="Any dietary restrictions or preferences"
    )
    price_range: str = Field(
        ..., 
        description="Preferred price range"
    )
    additional_preferences: str = Field(
        default="",
        description="Any additional preferences or notes"
    )

    def run(self):
        """
        Save the user's food preferences to a JSON file
        """
        preferences = {
            "cuisine_type": self.cuisine_type,
            "dietary_restrictions": self.dietary_restrictions,
            "price_range": self.price_range,
            "additional_preferences": self.additional_preferences
        }
        
        os.makedirs("data", exist_ok=True)
        with open("data/user_preferences.json", "w") as f:
            json.dump(preferences, f, indent=4)
        
        return "Preferences saved successfully"

if __name__ == "__main__":
    tool = SavePreferences(
        cuisine_type="Italian",
        dietary_restrictions="Vegetarian",
        price_range="$$",
        additional_preferences="Prefer outdoor seating"
    )
    print(tool.run()) 