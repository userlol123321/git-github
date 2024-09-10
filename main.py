import random
 
responses = [
    "I'm not a fan of Mondays either.",
    "I wish I could nap like a cat right now.",
    "Why do humans drink so much coffee?",
    "I once met a bug who thought it was a feature.",
    "I would tell you a joke, but all my bytes are tied up!",
]
 
print("You: Hey, computer!")
print(f"Computer: {random.choice(responses)}")