#!/bin/bash

# Startup script for Multi-Agent Haiku Web Interface

echo "🎋 Starting Multi-Agent Haiku System Web Interface..."
echo ""

# Activate virtual environment
source venv/bin/activate

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Please create a .env file with your ANTHROPIC_API_KEY"
    echo "You can copy .env.example: cp .env.example .env"
    exit 1
fi

# Launch Streamlit
echo "🚀 Launching web interface..."
echo "📍 Access at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py
