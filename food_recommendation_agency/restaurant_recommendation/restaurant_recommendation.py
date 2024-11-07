from agency_swarm import Agent
from .tools.search_restaurants import SearchRestaurants
from .tools.save_recommendation import SaveRecommendation

class RestaurantRecommendation(Agent):
    def __init__(self):
        super().__init__(
            name="Restaurant Recommendation",
            description="Provides restaurant recommendations based on user preferences",
            instructions="./instructions.md",
            tools=[SearchRestaurants, SaveRecommendation],
            temperature=0.7,
            max_prompt_tokens=4000,
        ) 