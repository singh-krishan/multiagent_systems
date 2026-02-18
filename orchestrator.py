"""
Orchestrator for Multi-Agent Haiku Refinement System
Coordinates interaction between HaikuAgent and CritiqueAgent
"""

from haiku_agent import HaikuAgent
from critique_agent import CritiqueAgent


class Orchestrator:
    """Orchestrates round-robin interaction between HaikuAgent and CritiqueAgent."""

    def __init__(self):
        """Initialize the orchestrator with both agents."""
        self.haiku_agent = HaikuAgent()
        self.critique_agent = CritiqueAgent()

    def run(self, topic="nature", max_turns=4):
        """
        Run the multi-agent refinement session.

        Args:
            topic (str): The topic for the haiku
            max_turns (int): Number of turns to run (alternating between agents)

        Returns:
            dict: History of the session with all turns
        """
        # Initialize tracking variables
        current_haiku = None
        current_critique = None
        history = {
            "topic": topic,
            "max_turns": max_turns,
            "turns": []
        }

        # Print session header
        print("=" * 60)
        print("MULTI-AGENT HAIKU REFINEMENT SESSION")
        print(f"Topic: {topic}")
        print(f"Max Turns: {max_turns}")
        print("=" * 60)
        print()

        # Main round-robin loop
        approved = False
        for turn in range(1, max_turns + 1):
            if turn % 2 == 1:  # Odd turns: Generate haiku
                print(f"Turn {turn}: HaikuAgent - Generating Haiku")
                print("-" * 60)

                # Generate haiku (with critique if available)
                current_haiku = self.haiku_agent.write_haiku(
                    topic=topic,
                    critique=current_critique
                )

                print(current_haiku)
                print()

                # Record in history
                history["turns"].append({
                    "turn": turn,
                    "agent": "HaikuAgent",
                    "action": "generate",
                    "output": current_haiku
                })

            else:  # Even turns: Critique haiku
                print(f"Turn {turn}: CritiqueAgent - Providing Critique")
                print("-" * 60)

                # Critique the current haiku
                current_critique = self.critique_agent.critique_haiku(current_haiku)

                print(current_critique)
                print()

                # Record in history
                history["turns"].append({
                    "turn": turn,
                    "agent": "CritiqueAgent",
                    "action": "critique",
                    "output": current_critique
                })

                # Check if haiku was approved
                if current_critique.startswith("APPROVED:"):
                    approved = True
                    print("🎉 Haiku has been APPROVED! Stopping early.")
                    print()
                    break

        # Print session footer
        print("=" * 60)
        print("SESSION COMPLETE")
        print("=" * 60)
        print()

        if approved:
            print(f"Final Haiku (APPROVED after {len(history['turns'])} turns):")
        else:
            print(f"Final Haiku (after {len(history['turns'])} turns):")

        print(current_haiku)
        print()

        # Store final haiku and approval status in history
        history["final_haiku"] = current_haiku
        history["approved"] = approved
        history["actual_turns"] = len(history['turns'])

        return history

    def get_summary(self, history):
        """
        Get a formatted summary of the session history.

        Args:
            history (dict): Session history from run()

        Returns:
            str: Formatted summary
        """
        summary = f"\nSession Summary:\n"
        summary += f"Topic: {history['topic']}\n"
        summary += f"Total Turns: {history['max_turns']}\n\n"

        for turn_data in history["turns"]:
            summary += f"Turn {turn_data['turn']} ({turn_data['agent']} - {turn_data['action']}):\n"
            summary += f"{turn_data['output']}\n\n"

        summary += f"Final Result:\n{history['final_haiku']}\n"

        return summary


# Run the orchestrator
if __name__ == "__main__":
    # Create the orchestrator
    orchestrator = Orchestrator()

    # Get user input for topic and turns
    print("Welcome to the Multi-Agent Haiku Refinement System!")
    print()

    topic = input("Enter haiku topic (or press Enter for 'nature'): ").strip()
    if not topic:
        topic = "nature"

    turns_input = input("Enter max turns (even number recommended, or press Enter for 4): ").strip()
    if not turns_input:
        max_turns = 4
    else:
        max_turns = int(turns_input)

    print()

    # Run the session
    history = orchestrator.run(topic=topic, max_turns=max_turns)

    # Optionally save history to file
    save = input("\nSave session history to file? (y/n): ").strip().lower()
    if save == 'y':
        import json
        filename = f"haiku_session_{topic.replace(' ', '_')}.json"
        with open(filename, 'w') as f:
            json.dump(history, f, indent=2)
        print(f"Session saved to {filename}")
