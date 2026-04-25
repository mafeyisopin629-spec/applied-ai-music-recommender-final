from recommender import load_songs, UserProfile, Recommender


def run_test(recommender, name, user, should_block=False):
    print("\n" + "=" * 50)
    print(f"TEST: {name}")
    print("=" * 50)

    result = recommender.agent_recommend(user, k=5)

    if should_block:
        if result["status"] == "blocked":
            print("✅ PASSED - Guardrail correctly blocked invalid input")
            for err in result["errors"]:
                print("-", err)
            return True
        print("❌ FAILED - Invalid input was not blocked")
        return False

    if result["status"] == "success" and result["recommendations"]:
        print("✅ PASSED")
        print("Top recommendation:", result["recommendations"][0]["song"].title)
        print("Self-check:", result["self_check"]["message"])
        return True

    print("❌ FAILED")
    return False


def main():
    songs = load_songs("data/songs.csv")
    recommender = Recommender(songs)

    tests = [
        ("High Energy Afrobeats", UserProfile("afrobeats", "happy", 0.9, False), False),
        ("Chill Lofi", UserProfile("lofi", "calm", 0.2, True), False),
        ("Conflicting Profile", UserProfile("electronic", "sad", 0.95, False), False),
        ("Invalid Input Guardrail", UserProfile("pop", "happy", 2.0, True), True),
    ]

    passed = 0

    for name, user, should_block in tests:
        if run_test(recommender, name, user, should_block):
            passed += 1

    print("\n" + "=" * 50)
    print(f"FINAL SCORE: {passed}/{len(tests)} tests passed")
    print("=" * 50)


if __name__ == "__main__":
    main()
