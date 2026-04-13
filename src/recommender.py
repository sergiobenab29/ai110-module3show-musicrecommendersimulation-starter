from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs.csv and return a list of dicts with numeric fields cast to int/float."""
    import csv
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row["id"].strip().isdigit():
                continue
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    int(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """Score a single song against user preferences and return (score, explanation)."""
    score = 0.0
    reasons = []

    # Genre match (+2.0)
    if song["genre"].lower() == user_prefs.get("genre", "").lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match (+1.0)
    if song["mood"].lower() == user_prefs.get("mood", "").lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy proximity (up to +1.5)
    if "energy" in user_prefs:
        energy_points = 1.5 * (1 - abs(song["energy"] - user_prefs["energy"]))
        score += energy_points
        reasons.append(f"energy proximity (+{energy_points:.2f})")

    # Valence proximity (up to +1.0)
    if "target_valence" in user_prefs:
        valence_points = 1.0 * (1 - abs(song["valence"] - user_prefs["target_valence"]))
        score += valence_points
        reasons.append(f"valence proximity (+{valence_points:.2f})")

    # Tempo proximity (up to +0.5)
    if "target_tempo_bpm" in user_prefs:
        tempo_points = 0.5 * (1 - abs(song["tempo_bpm"] - user_prefs["target_tempo_bpm"]) / 100)
        tempo_points = max(0.0, tempo_points)
        score += tempo_points
        reasons.append(f"tempo proximity (+{tempo_points:.2f})")

    explanation = ", ".join(reasons) if reasons else "no strong match"
    return score, explanation


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song in the catalog, sort by score descending, and return the top k."""
    scored = []
    for song in songs:
        score, explanation = score_song(user_prefs, song)
        scored.append((song, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
