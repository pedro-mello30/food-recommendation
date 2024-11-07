from agency_swarm import Agent
from .tools.manage_request import ManageRequest

class RecommendationManager(Agent):
    def __init__(self):
        super().__init__(
            name="Recommendation Manager",
            description="Manages the overall food recommendation process and coordinates between agents",
            instructions="./instructions.md",
            tools=[ManageRequest],
            temperature=0.7,
            max_prompt_tokens=4000,
        ) 