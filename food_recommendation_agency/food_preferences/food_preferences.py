from agency_swarm import Agent
from .tools.save_preferences import SavePreferences
from .tools.get_preferences import GetPreferences

class FoodPreferences(Agent):
    def __init__(self):
        super().__init__(
            name="Food Preferences",
            description="Handles user food preferences and dietary restrictions",
            instructions="./instructions.md",
            tools=[SavePreferences, GetPreferences],
            temperature=0.7,
            max_prompt_tokens=4000,
        ) 