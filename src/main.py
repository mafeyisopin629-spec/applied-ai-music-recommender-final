"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        {
            "name": "High-Energy Afrobeats",
            "prefs": {
                "favorite_genre": "afrobeats",
                "favorite_mood": "happy",
                "target_energy": 0.8,
                "likes_acoustic": False,
            },
        },
        {
            "name": "Chill Lofi",
            "prefs": {
                "favorite_genre": "lofi",
                "favorite_mood": "chill",
                "target_energy": 0.3,
                "likes_acoustic": True,
            },
        },
        {
            "name": "Conflicting Profile",
            "prefs": {
                "favorite_genre": "rock",
                "favorite_mood": "sad",
                "target_energy": 0.9,
                "likes_acoustic": False,
            },
        },
    ]

    for profile in profiles:
        print("\n" + "=" * 50)
        print(f"Profile: {profile['name']}")
        print("=" * 50)

        recommendations = recommend_songs(profile["prefs"], songs, k=5)

        print("\nTop recommendations:\n")
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{i}. {song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"   Because: {explanation}")
            print()
if __name__ == "__main__":
    main()