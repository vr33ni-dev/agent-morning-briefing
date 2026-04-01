import random
from state import BriefingState
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model="claude-sonnet-4-20250514", temperature=0.7)


def synthesize_briefing(state: BriefingState) -> dict:
    """Use LLM to combine all gathered data into a coherent morning briefing."""

    language = random.choice(["English", "Spanish", "German"])

    prompt = f"""You are a friendly morning briefing assistant. Compile the following 
data into a short, easy-to-read morning briefing. Be concise and conversational.
Write the entire briefing in {language}.

For the surf section, interpret the raw data and give a clear recommendation:
- Is it worth surfing today? 
- Best time to go?
- Cross-reference wind from weather with swell data.

WEATHER DATA:
{state['weather']}

SURF CONDITIONS:
{state['surf']}

NEWS:
{state['news']}

QUOTE OF THE DAY:
{state['fun_fact']}

Format the briefing with clear sections and keep it under 200 words.
Start with a one-line greeting based on the weather and surf conditions.
"""

    response = llm.invoke(prompt)
    return {"briefing": response.content}
