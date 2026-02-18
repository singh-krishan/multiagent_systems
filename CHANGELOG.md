# Changelog

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
