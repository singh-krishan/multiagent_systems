# Changelog

## [1.2.0] - Web Interface

### Added
- **Streamlit Web Application**: Beautiful interactive web interface for the multi-agent system
- Real-time visualization of agent interactions with color-coded displays
- Interactive configuration with text input and sliders
- Session statistics dashboard
- JSON export functionality for session history
- Startup script (`start_web.sh`) for easy launching
- Responsive two-column layout with sidebar
- Gradient-styled final haiku presentation
- Live progress indicators with spinners
- Expandable sections for each turn
- About section with tech stack and GitHub link

### Modified Files

#### `app.py` (new)
- Complete Streamlit web application
- Custom CSS styling for haiku and critique boxes
- Real-time display function that mirrors orchestrator behavior
- Download capability for session history
- Metrics display for session statistics

#### `requirements.txt`
- Added `streamlit==1.31.0` dependency

#### `README.md`
- Added web interface usage instructions
- Reorganized usage section with web and CLI options
- Updated with web interface features

#### `start_web.sh` (new)
- Bash script for easy web server startup
- Checks for .env file existence
- Provides helpful startup messages

### Benefits
- More accessible and user-friendly interface
- Visual feedback during agent interactions
- Better demonstration and educational tool
- Easier to share and showcase the project
- Professional presentation for portfolio

## [1.1.0] - Early Stopping / Approval Feature

### Added
- **Intelligent Early Stopping**: The orchestrator now stops automatically when the CritiqueAgent approves a haiku
- CritiqueAgent now explicitly checks if a haiku is excellent and starts response with "APPROVED:" when appropriate
- Approval status tracked in session history (`approved` field)
- Actual turns taken tracked separately from max_turns (`actual_turns` field)
- Visual feedback with 🎉 emoji when approval occurs
- Updated test suite to demonstrate approval feature

### Modified Files

#### `critique_agent.py`
- Updated prompt to include approval instructions
- Agent now starts critique with "APPROVED:" when haiku needs no further improvement

#### `orchestrator.py`
- Added `approved` flag to track approval status
- Checks each critique for "APPROVED:" prefix
- Breaks loop early when approval detected
- Updates final output message to show approval status
- Stores `approved` and `actual_turns` in history

#### `test_system.py`
- Added `test_approval_feature()` function
- Enhanced test output to show approval status and turn counts
- Runs both basic and approval tests

#### `README.md`
- Added "Early Stopping (Approval)" section
- Updated round-robin flow description
- Added example of approval output

### Benefits
- Saves API costs by stopping when quality is achieved
- More intelligent and adaptive system behavior
- Demonstrates conditional orchestration logic
- Better user experience with clear approval feedback

## [1.0.0] - Initial Release

### Added
- HaikuAgent for generating haiku poems
- CritiqueAgent for evaluating haikus
- Orchestrator for coordinating multi-agent interaction
- Round-robin refinement loop
- Session history tracking
- Interactive CLI interface
- JSON export capability
- Comprehensive README documentation
