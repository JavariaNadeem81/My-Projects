from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the values
username = os.getenv("USERNAME")
fav_color = os.getenv("FAV_COLOR")

# Show the welcome message
print(f"Welcome, {username}! Your favorite color is {fav_color} 💜")
