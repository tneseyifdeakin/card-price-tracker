import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("CARD_TRACKER_DB_PATH", "data/cards.db")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")