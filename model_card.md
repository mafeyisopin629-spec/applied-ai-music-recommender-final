# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

Answer
## Limitations and Bias

One weakness of this recommender is that it can over-prioritize some features more than others. In my tests, genre and energy often had a stronger impact on ranking than mood, especially when the user profile had conflicting preferences. This means the system may ignore emotionally relevant songs if they do not also fit the strongest numerical signals.

Another limitation is that the dataset is small, so the same songs can appear often across different profiles. This reduces variety and can create a filter bubble where the recommender keeps suggesting similar songs. The system is simple and explainable, but it does not yet have enough data or complexity to balance difficult preferences the way a real music platform would.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

Answer
## Evaluation

I tested the recommender with three different user profiles: High-Energy Afrobeats, Chill Lofi, and a Conflicting Profile. The High-Energy Afrobeats profile produced strong results, with songs like "Sunrise Parade" and "Golden Fire" ranking highest because they matched the user's preferred genre, mood, and energy level. The Chill Lofi profile also worked well, returning calmer and more acoustic songs such as "Library Rain" and "Midnight Coding."

The most interesting test was the Conflicting Profile, which combined a sad mood with very high energy. In this case, the system mostly prioritized genre, energy, and acoustic preference, while mood had less visible influence on the results. This showed that the recommender works best when preferences are consistent and becomes less balanced when the profile contains conflicting signals.

Overall, the results showed that the recommender is understandable and responsive, but also sensitive to its weights and limited by the size of the dataset.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  


Answers
## Model Name
VibeMatch Recommender 1.0

## Goal / Task
This system recommends songs based on a user’s preferences such as genre, mood, energy level, and whether they like acoustic music.

## Data Used
The system uses a dataset of 18 songs stored in a CSV file. Each song includes features like genre, mood, energy, tempo, valence, danceability, and acousticness. The dataset is small, which limits the variety of recommendations.

## Algorithm Summary
The system gives points to songs based on how well they match the user’s preferences. It adds points for matching genre and mood, and calculates a similarity score for energy based on how close it is to the user’s target. It also adds points if the song matches the user’s acoustic preference. The songs are then ranked from highest score to lowest.

## Observed Behavior / Biases
The system tends to prioritize genre and energy more than mood. In some cases, songs that do not match the user’s mood still rank highly if they match energy and genre. The system also repeats similar songs because the dataset is small, which can reduce diversity.

## Evaluation Process
I tested the system using three different user profiles: High-Energy Afrobeats, Chill Lofi, and a Conflicting Profile. The first two profiles produced accurate and expected results. The conflicting profile showed that the system struggles when preferences do not align well. I also tested how changing feature weights affected the rankings and saw noticeable differences.

## Intended Use and Non-Intended Use
This system is intended for simple music recommendation experiments and learning how recommender systems work. It should not be used for real-world recommendations because it uses a small dataset and simple logic that does not fully capture user preferences.

## Ideas for Improvement
- Increase the dataset size to improve recommendation diversity  
- Add more features like tempo matching or user history  
- Improve how conflicting preferences are handled so the system balances them better  

## Personal Reflection
The biggest thing I learned from this project is how simple scoring rules can still produce realistic recommendations. Using AI tools helped me move faster, especially for debugging and structuring the code, but I still had to carefully check the logic to make sure everything worked correctly.

One thing that surprised me is how even a basic algorithm can “feel” like a real recommender system when the scoring is done well. At the same time, I noticed that small changes in weights can significantly affect results.

If I were to extend this project, I would add more user behavior data and possibly implement collaborative filtering to make the recommendations more advanced and realistic.