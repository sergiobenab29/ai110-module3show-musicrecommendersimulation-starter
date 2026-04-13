"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os
from recommender import load_songs, recommend_songs

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "songs.csv")

PROFILES = [
    # --- Standard profiles ---
    {
        "label": "High-Energy Pop",
        "genre": "pop", "mood": "happy", "energy": 0.9,
        "target_valence": 0.85, "target_tempo_bpm": 128,
    },
    {
        "label": "Chill Lofi",
        "genre": "lofi", "mood": "chill", "energy": 0.35,
        "target_valence": 0.55, "target_tempo_bpm": 75,
    },
    {
        "label": "Deep Intense Rock",
        "genre": "rock", "mood": "intense", "energy": 0.92,
        "target_valence": 0.40, "target_tempo_bpm": 150,
    },
    # --- Adversarial / edge case profiles ---
    {
        "label": "EDGE: Conflicting Mood vs Energy (sad but high-energy)",
        "genre": "blues", "mood": "sad", "energy": 0.95,
        "target_valence": 0.20, "target_tempo_bpm": 160,
    },
    {
        "label": "EDGE: Genre not in catalog (country)",
        "genre": "country", "mood": "happy", "energy": 0.6,
        "target_valence": 0.70, "target_tempo_bpm": 100,
    },
]


def print_recommendations(user_prefs: dict, recommendations: list) -> None:
    print("\n" + "=" * 50)
    print(f"  {user_prefs['label']}")
    print(f"  genre={user_prefs.get('genre')}  mood={user_prefs.get('mood')}  energy={user_prefs.get('energy')}")
    print("=" * 50)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} by {song['artist']}")
        print(f"    Score : {score:.2f} / 6.00")
        print(f"    Why   : {explanation}")


def main() -> None:
    songs = load_songs(DATA_PATH)
    print(f"Loaded songs: {len(songs)}")

    for profile in PROFILES:
        recommendations = recommend_songs(profile, songs, k=5)
        print_recommendations(profile, recommendations)


if __name__ == "__main__":
    main()
