"""
Critique Agent for evaluating haiku poems using LLM (Anthropic SDK)
"""

import anthropic
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class CritiqueAgent:
    """A simple agent that uses Claude to critique haiku poems."""

    def __init__(self):
        """Initialize the agent with Anthropic client."""
        # Create the API client
        self.client = anthropic.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY")
        )

    def critique_haiku(self, haiku):
        """Provide constructive feedback on a haiku poem."""
        # Create a message asking for critique
        message = self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            messages=[
                {
                    "role": "user",
                    "content": f"""Please critique this haiku poem constructively:

{haiku}

Evaluate:
1. Syllable count (5-7-5 pattern)
2. Imagery and sensory details
3. Emotional impact
4. Seasonal reference (if present)
5. Overall effectiveness

If the haiku is excellent and needs no further improvement, start your response with "APPROVED:" and explain why it's great.

Otherwise, provide specific, actionable suggestions for improvement. Keep your critique concise but helpful."""
                }
            ]
        )

        # Get the critique from the response
        critique = message.content[0].text

        return critique


# Run the agent
if __name__ == "__main__":
    # Create the agent
    agent = CritiqueAgent()

    # Test with a sample haiku
    test_haiku = """Ancient pond stillness
Frog jumps into the water
Sound of the water"""

    print("Haiku to critique:\n")
    print(test_haiku)
    print("\n" + "="*60 + "\n")
    print("Critique:\n")
    print(agent.critique_haiku(test_haiku))
