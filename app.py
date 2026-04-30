import streamlit as st
from src.recommender import load_songs, UserProfile, Recommender

st.title("🎧 VibeAgent AI Music Recommender")

# Load songs
songs = load_songs("data/songs.csv")
recommender = Recommender(songs)

# Inputs
genre = st.text_input("Enter your favorite genre")
mood = st.text_input("Enter your mood")
energy = st.slider("Energy Level", 0.0, 1.0, 0.5)
acoustic = st.checkbox("Do you like acoustic music?")

# Button
if st.button("Recommend Songs"):
    user = UserProfile(
        favorite_genre=genre,
        favorite_mood=mood,
        target_energy=energy,
        likes_acoustic=acoustic
    )

    result = recommender.agent_recommend(user, k=5)

    if result["status"] == "blocked":
        st.error("Invalid input:")
        for err in result["errors"]:
            st.write(f"- {err}")
    else:
        st.subheader("🎵 Recommendations")

        for item in result["recommendations"]:
            song = item["song"]
            st.write(f"**{song.title} - {song.artist}**")
            st.write(f"Score: {item['score']}")
            st.write(f"Why: {item['explanation']}")
            st.write("---")
