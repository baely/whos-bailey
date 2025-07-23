# Who's Bailey? 🤖

An AI-powered personal assistant that answers questions about Bailey Butler using real-time data integration.

**🌐 Live Demo:** [https://baileybutler.au](https://baileybutler.au)

## What is this?

This is an interactive web application that serves as Bailey's digital persona - an AI assistant that can answer questions about Bailey's professional background, current activities, and personal data through various integrated APIs.

Ask questions like:
- "What's Bailey's work experience?"
- "Is Bailey in the office today?"
- "How many coffees has Bailey had today?"
- "What did Bailey spend money on recently?"

## Features

- **Real-time Data Integration**: Connects to live APIs for office status, banking transactions, and coffee consumption
- **AI-Powered Responses**: Uses Google Gemini for natural language understanding and contextual answers
- **Personal Data Access**: Integrates with UP Bank API for actual financial data
- **Office Tracking**: Real-time office presence detection
- **Coffee Analytics**: Tracks caffeine consumption patterns
- **Modern Web Interface**: Responsive design with smooth animations

## Tech Stack

**Backend:**
- Python 3.12 + Flask (async)
- Google AI Development Kit (ADK)
- Google Vertex AI / Gemini
- OpenAPI toolsets for external API integration

**Frontend:**
- Vanilla HTML/CSS/JavaScript
- Markdown parsing for rich responses

**Infrastructure:**
- Docker containerization
- Google Cloud Platform
- Docker secrets for credential management

**External APIs:**
- UP Bank API (banking data)
- baileyneeds.coffee (coffee tracking)
- isbaileybutlerintheoffice.today (office status)

## Quick Start

### Using Docker (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd whos-baioley

# Set up required secrets
echo "your-up-bank-token" | docker secret create up_token -

# Run the application
docker-compose up
```

### Local Development

```bash
# Install dependencies
uv sync

# Set up environment variables
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"

# Run the application
uv run python app.py
```

The application will be available at `http://localhost:8080`

## Configuration

The application requires:
- Google Cloud credentials for AI services
- UP Bank API token (stored as Docker secret `up_token`)
- Access to external APIs for office status and coffee tracking

## Project Structure

```
├── app.py                 # Main Flask web server
├── index.html            # Frontend interface
├── agent/
│   ├── agent.py          # AI agent with tool integrations
│   ├── coffee.yaml       # Coffee API specification
│   └── up.json          # UP Bank API specification
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml
```

## Security

- Banking credentials stored as Docker secrets
- No hardcoded API keys or sensitive data
- Proper authentication for external API access

---

*This is a personal project showcasing AI integration with real-world data sources. Built by Bailey Butler.*
