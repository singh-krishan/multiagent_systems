# Web Interface Quick Guide

## Starting the Web App

### Method 1: Using the startup script (Recommended)
```bash
./start_web.sh
```

### Method 2: Manual launch
```bash
source venv/bin/activate
streamlit run app.py
```

## Accessing the App

Open your browser and go to: **http://localhost:8501**

## Interface Overview

```
┌─────────────────────────────────────────────────────────┐
│  🎋 Multi-Agent Haiku Refinement System                │
├───────────────────────────────────┬─────────────────────┤
│                                   │  ⚙️ Configuration   │
│  Main Content Area                │                     │
│  ┌─────────────────────────────┐ │  Topic: [____]      │
│  │                             │ │                     │
│  │  Turn-by-turn display       │ │  Max Turns: [===]   │
│  │  with color-coded boxes:    │ │                     │
│  │                             │ │  [🚀 Generate]      │
│  │  🎋 Haiku (green boxes)     │ │                     │
│  │  💬 Critique (yellow boxes) │ │  ─────────────      │
│  │                             │ │  How it works       │
│  └─────────────────────────────┘ │  About              │
│                                   │  Tech Stack         │
│  ✨ Final Result                 │                     │
│  ┌─────────────────────────────┐ │                     │
│  │  [Final Haiku Display]      │ │                     │
│  └─────────────────────────────┘ │                     │
│                                   │                     │
│  📊 Session Statistics            │                     │
│  💾 Download Button               │                     │
└───────────────────────────────────┴─────────────────────┘
```

## Features Explained

### 1. Configuration Sidebar (Right)
- **Topic Input**: Type any topic (e.g., "spring rain", "mountain peak")
- **Max Turns Slider**: Set 2-10 turns (even numbers recommended)
- **How it Works**: Quick reference guide
- **About & Tech Stack**: Project information

### 2. Main Content Area (Left)

#### Generate Button
- Click "🚀 Generate Haiku" to start the session
- Shows spinner during processing
- Displays progress in real-time

#### Turn-by-Turn Display
Each turn appears in an expandable section:

**🎋 Haiku Turns (Odd: 1, 3, 5...)**
```
┌────────────────────────────────┐
│ Green box with haiku text      │
│ Pre-formatted for readability  │
└────────────────────────────────┘
```

**💬 Critique Turns (Even: 2, 4, 6...)**
```
┌────────────────────────────────┐
│ Yellow box with critique text  │
│ Detailed feedback from agent   │
└────────────────────────────────┘
```

#### Approval Detection
When approved, you'll see:
```
┌────────────────────────────────┐
│ 🎉 APPROVED after N turns!     │
│ (Green success box)            │
└────────────────────────────────┘
```

#### Final Haiku Display
Beautiful gradient box with:
- Large, centered text
- Purple gradient background
- White text for contrast
- Final refined haiku

#### Session Statistics
Four metric cards showing:
- **Topic**: The haiku subject
- **Turns Taken**: Actual turns completed
- **Max Turns**: Configured maximum
- **Status**: ✅ Approved or ⏹️ Completed

#### Download Section
- Click "Download Session History (JSON)"
- Gets a timestamped JSON file with full session data
- Includes all turns, final haiku, and metadata

## Color Coding

| Color | Element | Meaning |
|-------|---------|---------|
| 🟢 Green | Haiku Box | Generated poem |
| 🟡 Yellow | Critique Box | Agent feedback |
| 🟢 Green (light) | Approval Badge | Haiku approved |
| 🟣 Purple Gradient | Final Haiku | Final result display |

## Tips for Best Experience

### 1. Topic Selection
- **Specific topics** work better: "autumn maple leaves" > "nature"
- **Seasonal references** help: "winter frost", "spring cherry blossoms"
- **Sensory topics** inspire: "ocean waves", "morning coffee"

### 2. Max Turns Configuration
- **2 turns**: Quick test (1 haiku + 1 critique)
- **4 turns**: Standard (2 generation cycles with critique)
- **6 turns**: Extended refinement
- **8-10 turns**: Deep iteration (may approve early)

### 3. Watching Progress
- Keep expandable sections open to watch real-time
- Collapse earlier turns to focus on current iteration
- Notice how critiques influence next generation

### 4. Session Management
- Each click generates a NEW session
- Download history before starting a new one
- JSON files include timestamps for organization

## Keyboard Shortcuts

Streamlit provides these shortcuts:
- **`R`**: Rerun the app
- **`C`**: Clear cache
- **`?`**: Show keyboard shortcuts

## Troubleshooting

### App won't start
```bash
# Check if virtual environment is activated
which python
# Should show: .../venv/bin/python

# Check if Streamlit is installed
pip list | grep streamlit

# Reinstall if needed
pip install streamlit==1.31.0
```

### Port already in use
```bash
# Kill existing Streamlit process
pkill -f streamlit

# Or use a different port
streamlit run app.py --server.port 8502
```

### API key errors
```bash
# Verify .env file exists
cat .env

# Should contain:
ANTHROPIC_API_KEY=sk-ant-...

# Check it's being loaded
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('ANTHROPIC_API_KEY')[:10])"
```

### Slow performance
- API calls take 2-5 seconds each
- Multiple turns = multiple API calls
- This is normal for LLM interactions
- Consider reducing max_turns for faster demos

## Stopping the Server

### Method 1: In terminal
Press **`Ctrl+C`** in the terminal running Streamlit

### Method 2: Kill process
```bash
# Find the process
lsof -i :8501

# Kill it
kill [PID]

# Or kill all Streamlit
pkill -f streamlit
```

## Advanced Customization

### Change Port
```bash
streamlit run app.py --server.port 8080
```

### Auto-open Browser
```bash
streamlit run app.py --server.headless false
```

### Disable CORS (for remote access)
```bash
streamlit run app.py --server.enableCORS false
```

### Custom Theme
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#4CAF50"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

## Production Deployment

To deploy this app publicly, you can use:

### Streamlit Cloud (Free)
1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Connect your repository
4. Deploy!

### Other Options
- **Heroku**: Free tier available
- **Google Cloud Run**: Containerized deployment
- **AWS EC2**: Full control
- **Railway**: Simple deployment

Remember to set `ANTHROPIC_API_KEY` as an environment variable (NOT in code) for production!

## Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Anthropic API Docs](https://docs.anthropic.com)
