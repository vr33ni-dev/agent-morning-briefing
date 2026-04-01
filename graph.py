from langgraph.graph import StateGraph, START, END
from state import BriefingState
from nodes import fetch_weather, fetch_surf, fetch_news, fetch_fun_fact
from synthesizer import synthesize_briefing


def build_graph():
    graph = StateGraph(BriefingState)

    # Add all nodes
    graph.add_node("weather", fetch_weather)
    graph.add_node("surf", fetch_surf)
    graph.add_node("news", fetch_news)
    graph.add_node("fun_fact", fetch_fun_fact)
    graph.add_node("synthesize", synthesize_briefing)

    # Data-gathering nodes run in parallel from START
    graph.add_edge(START, "weather")
    graph.add_edge(START, "surf")
    graph.add_edge(START, "news")
    graph.add_edge(START, "fun_fact")

    # All data nodes feed into the synthesizer
    graph.add_edge("weather", "synthesize")
    graph.add_edge("surf", "synthesize")
    graph.add_edge("news", "synthesize")
    graph.add_edge("fun_fact", "synthesize")

    # Synthesizer outputs the final briefing
    graph.add_edge("synthesize", END)

    return graph.compile()
