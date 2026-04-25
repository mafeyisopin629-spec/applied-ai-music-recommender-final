from recommender import load_songs, UserProfile, Recommender


def run_profile(recommender, profile_name, user):
    print("\n" + "=" * 60)
    print(f"Profile: {profile_name}")
    print("=" * 60)

    result = recommender.agent_recommend(user, k=5)

    print("\n--- SYSTEM TRACE ---")
    for step in result["trace"]:
        print(step)

    if result["status"] == "blocked":
        print("\n❌ Guardrail blocked this input:")
        for error in result["errors"]:
            print(f"- {error}")
        return

    print("\n🎵 TOP RECOMMENDATIONS:\n")

    for i, item in enumerate(result["recommendations"], start=1):
        song = item["song"]
        print(f"{i}. {song.title} by {song.artist}")
        print(f"   Score: {item['score']}")
        print(f"   Why: {item['explanation']}\n")

    print("🔍 SELF CHECK:")
    print(result["self_check"]["message"])


def main():
    print("Loading songs from data/songs.csv...")
    songs_data = load_songs("data/songs.csv")
    songs = songs_data
    print(f"Loaded songs: {len(songs)}")

    recommender = Recommender(songs)

    profiles = [
        (
            "High-Energy Afrobeats",
            UserProfile("afrobeats", "happy", 0.90, False),
        ),
        (
            "Chill Lofi",
            UserProfile("lofi", "chill", 0.35, True),
        ),
        (
            "Conflicting Profile",
            UserProfile("electronic", "sad", 0.95, False),
        ),
        (
            "Invalid Guardrail Example",
            UserProfile("pop", "happy", 1.50, False),
        ),
    ]

    for name, user in profiles:
        run_profile(recommender, name, user)


if __name__ == "__main__":
    main()