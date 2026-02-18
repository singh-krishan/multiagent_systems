"""
Super Basic Haiku Agent using LLM (Anthropic SDK)
"""

import anthropic
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class HaikuAgent:
    """A simple agent that uses Claude to write haiku poems."""

    def __init__(self):
        """Initialize the agent with Anthropic client."""
        # Create the API client
        self.client = anthropic.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY")
        )

    def write_haiku(self, topic="nature", critique=None):
        """Ask Claude to write a haiku."""
        # Build prompt conditionally based on whether critique is provided
        if critique:
            prompt = f"""Based on this critique:

{critique}

Please write an improved haiku about {topic} that addresses the feedback. Just the haiku, nothing else."""
        else:
            prompt = f"Write a haiku poem about {topic}. Just the haiku, nothing else."

        # Create a message asking for a haiku
        message = self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=200,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # Get the haiku from the response
        haiku = message.content[0].text

        return haiku


# Run the agent
if __name__ == "__main__":
    # Create the agent
    agent = HaikuAgent()

    # Generate a haiku
    print("Here is your haiku:\n")
    print(agent.write_haiku(topic="nature"))
