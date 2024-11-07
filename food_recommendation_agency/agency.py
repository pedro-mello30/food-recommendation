from agency_swarm import Agency
from agency_swarm import set_openai_key
from recommendation_manager.recommendation_manager import RecommendationManager
from food_preferences.food_preferences import FoodPreferences
from restaurant_recommendation.restaurant_recommendation import RestaurantRecommendation
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set OpenAI API key
set_openai_key(os.getenv("OPENAI_API_KEY"))

# Initialize agents
manager = RecommendationManager()
preferences = FoodPreferences()
recommendations = RestaurantRecommendation()

# Create agency with communication flows
agency = Agency(
    [
        manager,  # Entry point for user communication
        [manager, preferences],  # Manager can communicate with Preferences
        [manager, recommendations],  # Manager can communicate with Recommendations
        [preferences, recommendations]  # Preferences can communicate with Recommendations
    ],
    shared_instructions="agency_manifesto.md",
    temperature=0.7,
    max_prompt_tokens=4000
)

if __name__ == "__main__":
    agency.run_demo() 