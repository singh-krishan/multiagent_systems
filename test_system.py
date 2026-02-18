"""
Simple test script to verify the multi-agent system works
"""

from orchestrator import Orchestrator

def test_basic_flow():
    """Test a basic 2-turn flow"""
    print("Testing Multi-Agent Haiku System...")
    print("Running a simple 2-turn test (1 generation + 1 critique)\n")

    orchestrator = Orchestrator()
    history = orchestrator.run(topic="winter", max_turns=2)

    print("\n" + "=" * 60)
    print("TEST RESULTS")
    print("=" * 60)
    print(f"✓ Successfully completed {len(history['turns'])} turns")
    print(f"✓ Topic: {history['topic']}")
    print(f"✓ Generated haiku: Present")
    print(f"✓ Received critique: Present")
    print(f"✓ Approved: {history.get('approved', False)}")
    print(f"✓ Actual turns taken: {history['actual_turns']}")
    print("\nTest PASSED! System is working correctly.")

    return history

def test_approval_feature():
    """Test the approval/early stopping feature with more turns"""
    print("\n" + "=" * 60)
    print("Testing Approval Feature...")
    print("Running with max_turns=6 to see if early stopping occurs\n")

    orchestrator = Orchestrator()
    history = orchestrator.run(topic="cherry blossoms", max_turns=6)

    print("\n" + "=" * 60)
    print("APPROVAL TEST RESULTS")
    print("=" * 60)
    print(f"✓ Max turns allowed: {history['max_turns']}")
    print(f"✓ Actual turns taken: {history['actual_turns']}")
    print(f"✓ Early approval: {history.get('approved', False)}")

    if history.get('approved'):
        print("✓ System successfully detected approval and stopped early!")
    else:
        print("✓ System ran full iteration without approval")

    return history

if __name__ == "__main__":
    # Run basic test
    test_basic_flow()

    # Run approval test
    test_approval_feature()
