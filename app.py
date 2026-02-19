"""
Streamlit Web Interface for Multi-Agent Haiku Refinement System
"""

import streamlit as st
from orchestrator import Orchestrator
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Multi-Agent Haiku System",
    page_icon="🎋",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .haiku-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin: 10px 0;
    }
    .critique-box {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        margin: 10px 0;
    }
    .approved-box {
        background-color: #d4edda;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 10px 0;
    }
    .final-haiku {
        font-size: 1.3em;
        font-style: italic;
        text-align: center;
        padding: 30px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🎋 Multi-Agent Haiku Refinement System")
st.markdown("""
This interactive demo uses two AI agents to collaboratively create and refine haiku poems:
- **HaikuAgent**: Generates beautiful haiku poems
- **CritiqueAgent**: Provides expert feedback and can approve excellent haikus
- **Orchestrator**: Coordinates the iterative refinement process
""")

# Sidebar for configuration
st.sidebar.header("⚙️ Configuration")

topic = st.sidebar.text_input(
    "Haiku Topic",
    value="autumn leaves",
    help="What should the haiku be about?"
)

max_turns = st.sidebar.slider(
    "Maximum Turns",
    min_value=2,
    max_value=10,
    value=6,
    step=2,
    help="Number of generation/critique cycles (even numbers recommended)"
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### How it works:
1. **Odd turns**: HaikuAgent generates/improves haiku
2. **Even turns**: CritiqueAgent evaluates and may approve
3. **Early stopping**: Stops when haiku is approved
""")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # Run button
    if st.button("🚀 Generate Haiku", type="primary", use_container_width=True):
        # Create orchestrator
        orchestrator = Orchestrator()

        # Create containers for real-time updates
        status_container = st.empty()
        conversation_container = st.container()

        # Track progress
        with status_container:
            with st.spinner(f"Starting multi-agent session on topic: '{topic}'..."):
                # Run the session with custom display
                history = run_with_streamlit_display(
                    orchestrator,
                    topic,
                    max_turns,
                    conversation_container
                )

        # Clear status
        status_container.empty()

        # Display final result
        st.markdown("---")
        st.subheader("✨ Final Result")

        if history.get('approved'):
            st.markdown(f"""
                <div class='approved-box'>
                    <h3>🎉 APPROVED after {history['actual_turns']} turns!</h3>
                </div>
                """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class='final-haiku'>
                {history['final_haiku'].replace(chr(10), '<br>')}
            </div>
            """, unsafe_allow_html=True)

        # Statistics
        st.markdown("---")
        st.subheader("📊 Session Statistics")
        stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

        with stat_col1:
            st.metric("Topic", topic)
        with stat_col2:
            st.metric("Turns Taken", history['actual_turns'])
        with stat_col3:
            st.metric("Max Turns", history['max_turns'])
        with stat_col4:
            st.metric("Status", "✅ Approved" if history.get('approved') else "⏹️ Completed")

        # Download session history
        st.markdown("---")
        st.subheader("💾 Download Session")

        json_data = json.dumps(history, indent=2)
        st.download_button(
            label="Download Session History (JSON)",
            data=json_data,
            file_name=f"haiku_session_{topic.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )

with col2:
    st.subheader("ℹ️ About")
    st.markdown("""
    This system demonstrates:
    - Multi-agent coordination
    - Iterative refinement
    - Natural language critique
    - Conditional orchestration
    - Early stopping optimization
    """)

    st.markdown("---")
    st.subheader("🔧 Tech Stack")
    st.markdown("""
    - **Claude AI** (Haiku model)
    - **Python** orchestration
    - **Streamlit** web interface
    - **Anthropic SDK**
    """)

    st.markdown("---")
    st.markdown("""
    <small>
    Built as a learning project for multi-agent systems.
    <a href="https://github.com/singh-krishan/multiagent_systems" target="_blank">View on GitHub</a>
    </small>
    """, unsafe_allow_html=True)


def run_with_streamlit_display(orchestrator, topic, max_turns, container):
    """
    Run the orchestrator with Streamlit display instead of console output.
    """
    # Initialize tracking variables
    current_haiku = None
    current_critique = None
    history = {
        "topic": topic,
        "max_turns": max_turns,
        "turns": []
    }
    approved = False

    # Display in container
    with container:
        st.markdown(f"### 🎯 Session: {topic}")

        # Main round-robin loop
        for turn in range(1, max_turns + 1):
            if turn % 2 == 1:  # Odd turns: Generate haiku
                with st.expander(f"🎋 Turn {turn}: HaikuAgent - Generating Haiku", expanded=True):
                    with st.spinner("Generating haiku..."):
                        # Generate haiku (with critique if available)
                        current_haiku = orchestrator.haiku_agent.write_haiku(
                            topic=topic,
                            critique=current_critique
                        )

                    st.markdown(f"""
                        <div class='haiku-box'>
                            <pre style='margin:0; font-size:1.1em; white-space: pre-wrap;'>{current_haiku}</pre>
                        </div>
                        """, unsafe_allow_html=True)

                    # Record in history
                    history["turns"].append({
                        "turn": turn,
                        "agent": "HaikuAgent",
                        "action": "generate",
                        "output": current_haiku
                    })

            else:  # Even turns: Critique haiku
                with st.expander(f"💬 Turn {turn}: CritiqueAgent - Providing Critique", expanded=True):
                    with st.spinner("Analyzing haiku..."):
                        # Critique the current haiku
                        current_critique = orchestrator.critique_agent.critique_haiku(current_haiku)

                    st.markdown(f"""
                        <div class='critique-box'>
                            {current_critique}
                        </div>
                        """, unsafe_allow_html=True)

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
                        st.success("🎉 Haiku has been APPROVED! Stopping early.")
                        break

    # Store final haiku and approval status in history
    history["final_haiku"] = current_haiku
    history["approved"] = approved
    history["actual_turns"] = len(history['turns'])

    return history


# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p>Multi-Agent Haiku Refinement System | Built with Claude AI & Streamlit</p>
    </div>
    """, unsafe_allow_html=True)
