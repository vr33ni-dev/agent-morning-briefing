from dotenv import load_dotenv

load_dotenv()

from graph import build_graph


def main():
    agent = build_graph()

    # ===== CONFIGURE THESE FOR YOUR SETUP =====
    initial_state = {
        "location": {
            "lat": 13.6894,        # San Salvador
            "lon": -89.1872,
            "name": "San Salvador",
        },
        "surf_spot": {
            "lat": 13.4833,        # El Zonte, El Salvador
            "lon": -89.3833,
            "name": "El Zonte",
        },
        "topics": ["tech", "politics", "stocks"],
        # These will be filled by the nodes:
        "weather": "",
        "surf": "",
        "news": "",
        "fun_fact": "",
        "briefing": "",
    }
    # ==========================================

    print("Gathering your morning briefing...\n")
    result = agent.invoke(initial_state)
    print(result["briefing"])


if __name__ == "__main__":
    main()
