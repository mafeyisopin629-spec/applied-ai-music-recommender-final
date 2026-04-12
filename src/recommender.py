from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv


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
        """Return the top-k recommended songs for a user."""
        scored_songs = []

        for song in self.songs:
            score = 0.0

            if song.genre.lower() == user.favorite_genre.lower():
                score += 2.0

            if song.mood.lower() == user.favorite_mood.lower():
                score += 1.0

            energy_score = max(0.0, 1.0 - abs(song.energy - user.target_energy))
            score += energy_score

            if user.likes_acoustic:
                score += song.acousticness
            else:
                score += (1.0 - song.acousticness)

            scored_songs.append((song, score))

        scored_songs.sort(key=lambda item: item[1], reverse=True)
        return [song for song, _ in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a short explanation for why a song was recommended."""
        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("genre match (+2.0)")

        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("mood match (+1.0)")

        energy_score = max(0.0, 1.0 - abs(song.energy - user.target_energy))
        reasons.append(f"energy similarity (+{energy_score:.2f})")

        if user.likes_acoustic:
            acoustic_score = song.acousticness
            reasons.append(f"acoustic preference match (+{acoustic_score:.2f})")
        else:
            acoustic_score = 1.0 - song.acousticness
            reasons.append(f"non-acoustic preference match (+{acoustic_score:.2f})")

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    print(f"Loading songs from {csv_path}...")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_score = max(0.0, 1.0 - abs(song["energy"] - user_prefs["target_energy"]))
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    likes_acoustic = user_prefs.get("likes_acoustic", False)
    if likes_acoustic:
        acoustic_score = song["acousticness"]
        score += acoustic_score
        reasons.append(f"acoustic preference match (+{acoustic_score:.2f})")
    else:
        acoustic_score = 1.0 - song["acousticness"]
        score += acoustic_score
        reasons.append(f"non-acoustic preference match (+{acoustic_score:.2f})")

    return round(score, 2), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_results = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_results.append((song, score, explanation))

    scored_results.sort(key=lambda item: item[1], reverse=True)
    return scored_results[:k]