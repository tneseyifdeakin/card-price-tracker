from anthropic import Anthropic
from config import ANTHROPIC_API_KEY

client = Anthropic(api_key=ANTHROPIC_API_KEY)

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=256,
    system="You are a Sorcery: Contested Realm rules expert. Answer questions using ONLY the card data provided. If the information isn't in the provided data, say so.",
    messages=[
        {"role": "user", "content": """Here is the card data:
Name: Accursed Albatross
Element: Water
Cost: 3
Threshold: 1
Type: Minion - Beast
Power: 1
Defense: 1
Rarity: Ordinary

Question: What element is Accursed Albatross and how much does it cost to play?"""}
    ],
)

print(message.content[0].text)