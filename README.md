# Morning Briefing Agent

A LangGraph-powered agent that gathers weather, surf conditions, news, and a daily quote — then synthesizes them into a personalized morning briefing.

## How It Works

```
          ┌──────────────┐
          │    START      │
          └──────┬───────┘
                 │
    ┌────────────┼────────────┬────────────┐
    ▼            ▼            ▼            ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌──────────┐
│Weather │ │  Surf  │ │  News  │ │ Fun Fact │
│  Node  │ │  Node  │ │  Node  │ │   Node   │
└───┬────┘ └───┬────┘ └───┬────┘ └────┬─────┘
    │          │          │           │
    └──────────┼──────────┴───────────┘
               ▼
       ┌──────────────┐
       │ Synthesizer  │
       │    (LLM)     │
       └──────┬───────┘
              ▼
       ┌──────────────┐
       │     END      │
       └──────────────┘
```

The four data-gathering nodes run **in parallel**, then the synthesizer uses an LLM to combine everything into a coherent, conversational briefing with a surf recommendation.

## Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/morning-briefing-agent.git
cd morning-briefing-agent

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure your API keys
cp .env.example .env
# Edit .env with your keys
```

### API Keys Needed

| API | Cost | What it does |
|-----|------|-------------|
| [Anthropic](https://console.anthropic.com/settings/keys) | Pay-per-use | Powers the synthesizer LLM |
| [NewsAPI](https://newsapi.org/register) | Free tier (100 req/day) | Fetches news headlines |
| [Open-Meteo](https://open-meteo.com/) | Free, no key needed | Weather and surf data |
| [ZenQuotes](https://zenquotes.io/) | Free, no key needed | Daily quote |

## Configuration

Edit `src/main.py` to set your location, surf spot, and news topics:

```python
initial_state = {
    "location": {
        "lat": 13.6894,        # Your city
        "lon": -89.1872,
        "name": "San Salvador",
    },
    "surf_spot": {
        "lat": 13.4833,        # Your surf break
        "lon": -89.3833,
        "name": "El Zonte",
    },
    "topics": ["AI", "tech", "python"],
}
```

## Run

```bash
cd src
python main.py
```

## Automate It (Optional)

Run it every morning with a cron job:

```bash
# Edit crontab
crontab -e

# Add this line to run at 6:00 AM every day
0 6 * * * cd /path/to/morning-briefing-agent && ./venv/bin/python src/main.py >> briefing.log 2>&1
```

Or send it to yourself via email/Telegram/Slack — see the stretch goals below.

## Stretch Goals

- [ ] **Critique loop**: Add a node that checks if the briefing is too long or missing key info, loops back to rewrite
- [ ] **Delivery**: Send the briefing via email (SMTP), Telegram bot, or Slack webhook
- [ ] **Calendar**: Add a node that pulls today's events from Google Calendar
- [ ] **Tide data**: Add tide times alongside surf conditions
- [ ] **Historical tracking**: Save briefings to a file and track trends over time

## Built With

- [LangGraph](https://github.com/langchain-ai/langgraph) — Agent orchestration
- [Open-Meteo](https://open-meteo.com/) — Weather & marine data
- [NewsAPI](https://newsapi.org/) — News headlines
- [ZenQuotes](https://zenquotes.io/) — Daily quotes
