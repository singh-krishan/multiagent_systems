# Multi-Agent Haiku Refinement System

A learning project demonstrating multi-agent coordination using Claude AI. This system iteratively refines haiku poems through collaboration between specialized agents.

## Architecture

```
User → Orchestrator → HaikuAgent ⇄ CritiqueAgent
                ↓
         Round-robin loop (max_turns)
                ↓
        Refined haiku output
```

## Components

1. **HaikuAgent** (`haiku_agent.py`) - Generates haiku poems on a given topic
   - Can generate fresh haikus
   - Can generate improved haikus based on critique feedback

2. **CritiqueAgent** (`critique_agent.py`) - Provides constructive feedback on haikus
   - Evaluates syllable count (5-7-5 pattern)
   - Assesses imagery, emotional impact, and seasonal references
   - Provides actionable improvement suggestions

3. **Orchestrator** (`orchestrator.py`) - Manages round-robin interaction
   - Coordinates alternating turns between agents
   - Tracks conversation history
   - Displays formatted output

## Setup

1. Ensure you have a virtual environment activated:
   ```bash
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify your `.env` file has your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_key_here
   ```

## Usage

### Running the Full System

```bash
python orchestrator.py
```

You'll be prompted to enter:
- **Topic**: The subject for the haiku (e.g., "spring", "ocean", "moonlight")
- **Max Turns**: Number of iterations (even numbers recommended for balanced critique/generation)

### Example Session

```
Turn 1: HaikuAgent - Generating Haiku
------------------------------------------------------------
Cherry blossoms fall
Petals dance on spring breezes
Nature's brief beauty

Turn 2: CritiqueAgent - Providing Critique
------------------------------------------------------------
Good imagery and 5-7-5 structure. Consider adding more
specific sensory details...

Turn 3: HaikuAgent - Generating Haiku
------------------------------------------------------------
[Improved haiku based on critique]

Turn 4: CritiqueAgent - Providing Critique
------------------------------------------------------------
[Evaluation of improvements]
```

### Testing Individual Agents

Test the CritiqueAgent standalone:
```bash
python critique_agent.py
```

Test the HaikuAgent standalone:
```bash
python haiku_agent.py
```

## Round-Robin Flow

- **Odd turns (1, 3, 5...)**: HaikuAgent generates or refines haiku
- **Even turns (2, 4, 6...)**: CritiqueAgent provides feedback
- Each generation after the first incorporates previous critique
- **Early stopping**: If CritiqueAgent approves the haiku (starts response with "APPROVED:"), the session ends immediately, even if max_turns hasn't been reached

## Early Stopping (Approval)

The system features intelligent early stopping:

- When the CritiqueAgent determines a haiku is excellent and needs no improvement, it responds with "APPROVED:" at the start of its critique
- The orchestrator detects this and immediately ends the session
- This prevents unnecessary API calls and iterations once quality is achieved
- The session history tracks whether the haiku was approved or simply completed max_turns

Example:
```
Turn 4: CritiqueAgent - Providing Critique
------------------------------------------------------------
APPROVED: This haiku perfectly captures the essence of autumn
with vivid imagery and correct 5-7-5 syllable structure...

🎉 Haiku has been APPROVED! Stopping early.
```

## Customization

Modify the `orchestrator.py` main block to:
- Set default topics
- Change max_turns programmatically
- Customize output formatting
- Add additional processing of history
- Adjust the approval detection logic

## Learning Objectives

This project demonstrates:
- Multi-agent system coordination
- Iterative refinement through agent collaboration
- Stateful conversation management
- Modular agent design
- API integration with Claude AI

## Files

- `haiku_agent.py` - Haiku generation agent
- `critique_agent.py` - Haiku critique agent
- `orchestrator.py` - Multi-agent coordinator
- `requirements.txt` - Python dependencies
- `.env` - API key configuration (not tracked in git)
- `README.md` - This file

## Session History

The orchestrator can optionally save session history to JSON files for later analysis.
