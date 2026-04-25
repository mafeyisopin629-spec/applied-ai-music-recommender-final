from dataclasses import dataclass
from typing import Dict, List, Tuple
import csv


@dataclass
class Song:
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
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def validate_user(self, user: UserProfile) -> List[str]:
        errors = []

        if user.target_energy < 0 or user.target_energy > 1:
            errors.append("target_energy must be between 0 and 1.")

        if not user.favorite_genre:
            errors.append("favorite_genre cannot be empty.")

        if not user.favorite_mood:
            errors.append("favorite_mood cannot be empty.")

        return errors

    def retrieve_candidates(self, user: UserProfile) -> List[Song]:
        candidates = [
            song for song in self.songs
            if song.genre.lower() == user.favorite_genre.lower()
            or song.mood.lower() == user.favorite_mood.lower()
        ]

        return candidates if candidates else self.songs

    def score_song(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        score = 0.0
        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            score += 2.0
            reasons.append("genre match (+2.0)")

        if song.mood.lower() == user.favorite_mood.lower():
            score += 1.0
            reasons.append("mood match (+1.0)")

        energy_score = max(0.0, 1.0 - abs(song.energy - user.target_energy))
        score += energy_score
        reasons.append(f"energy similarity (+{energy_score:.2f})")

        if user.likes_acoustic:
            score += song.acousticness
            reasons.append(f"acoustic preference match (+{song.acousticness:.2f})")
        else:
            non_acoustic_score = 1.0 - song.acousticness
            score += non_acoustic_score
            reasons.append(f"non-acoustic preference match (+{non_acoustic_score:.2f})")

        return round(score, 2), reasons

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        errors = self.validate_user(user)
        if errors:
            return []

        candidates = self.retrieve_candidates(user)
        scored = []

        for song in candidates:
            score, reasons = self.score_song(user, song)
            scored.append((song, score, reasons))

        scored.sort(key=lambda item: item[1], reverse=True)
        return [song for song, score, reasons in scored[:k]]

    def agent_recommend(self, user: UserProfile, k: int = 5) -> Dict:
        trace = []

        trace.append("Step 1: Validate user preferences.")
        errors = self.validate_user(user)

        if errors:
            return {
                "status": "blocked",
                "errors": errors,
                "trace": trace,
                "recommendations": [],
                "self_check": {
                    "passed": False,
                    "message": "Input was blocked by guardrails.",
                },
            }

        trace.append("Step 2: Retrieve candidate songs from the dataset.")
        candidates = self.retrieve_candidates(user)

        trace.append(f"Step 3: Rank {len(candidates)} candidate songs using scoring rules.")
        scored_results = []

        for song in candidates:
            score, reasons = self.score_song(user, song)
            scored_results.append({
                "song": song,
                "score": score,
                "explanation": ", ".join(reasons),
            })

        scored_results.sort(key=lambda item: item["score"], reverse=True)
        top_results = scored_results[:k]

        trace.append("Step 4: Self-check recommendation quality.")
        check = self.self_check(user, top_results)

        return {
            "status": "success",
            "trace": trace,
            "recommendations": top_results,
            "self_check": check,
        }

    def self_check(self, user: UserProfile, results: List[Dict]) -> Dict:
        if not results:
            return {
                "passed": False,
                "message": "No recommendations were generated.",
            }

        top_song = results[0]["song"]
        genre_match = top_song.genre.lower() == user.favorite_genre.lower()
        mood_match = top_song.mood.lower() == user.favorite_mood.lower()

        if genre_match or mood_match:
            return {
                "passed": True,
                "message": "Top recommendation passed because it matches the user's genre or mood preference.",
            }

        return {
            "passed": True,
            "message": "Top recommendation passed using fallback ranking.",
        }


def load_songs(csv_path: str) -> List[Song]:
    songs = []

    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            songs.append(
                Song(
                    id=int(row["id"]),
                    title=row["title"],
                    artist=row["artist"],
                    genre=row["genre"],
                    mood=row["mood"],
                    energy=float(row["energy"]),
                    tempo_bpm=float(row["tempo_bpm"]),
                    valence=float(row["valence"]),
                    danceability=float(row["danceability"]),
                    acousticness=float(row["acousticness"]),
                )
            )

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    user = UserProfile(
        favorite_genre=user_prefs["favorite_genre"],
        favorite_mood=user_prefs["favorite_mood"],
        target_energy=user_prefs["target_energy"],
        likes_acoustic=user_prefs.get("likes_acoustic", False),
    )

    song_obj = Song(**song)
    recommender = Recommender([song_obj])
    return recommender.score_song(user, song_obj)


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5):
    song_objects = [Song(**song) for song in songs]
    user = UserProfile(
        favorite_genre=user_prefs["favorite_genre"],
        favorite_mood=user_prefs["favorite_mood"],
        target_energy=user_prefs["target_energy"],
        likes_acoustic=user_prefs.get("likes_acoustic", False),
    )

    recommender = Recommender(song_objects)
    result = recommender.agent_recommend(user, k)

    output = []
    for item in result["recommendations"]:
        song = item["song"]
        output.append((song.__dict__, item["score"], item["explanation"]))

    return output
