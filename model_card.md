# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**SoundMatch 1.0**

---

## 2. Intended Use

SoundMatch tries to predict which songs a user will enjoy based on their preferred genre, mood, and energy level. It does this by scoring every song in the catalog and returning the ones that are the closest match. It is built for classroom exploration only and is not meant for real users or a real product.

---

## 3. How the Model Works

The system looks at each song in the catalog and gives it a score based on how well it matches the user's preferences. It awards bonus points for an exact genre match and an exact mood match. It also checks how close the song's energy, emotional tone (valence), and tempo are to what the user wants the closer, the more points. Songs are then ranked from highest to lowest score, and the top results are shown.

---

## 4. Data

The catalog has 18 songs. Each song has a genre, mood, energy level, tempo, valence, danceability, and acousticness. Genres include pop, lofi, rock, jazz, metal, classical, blues, folk, reggae, and more. Most genres only appear once or twice, which limits how well the system works for niche listeners. The dataset does not include lyrics, release year, or artist popularity.

---

## 5. Strengths

The system works best for users whose preferences match common genres in the catalog like pop or lofi, since those have more songs to compare. When genre, mood, and energy all line up, the top result feels very accurate. Every recommendation comes with a reason, so it is easy to understand why a song was picked.

---

## 6. Limitations and Bias

The biggest weakness is that most genres in the catalog only have one song. This means a metal or jazz fan will almost never get a great genre match, while a pop or lofi fan gets multiple options. The system also ignores the `acousticness` and `danceability` fields entirely. Finally, if a user types a mood like `"mellow"` instead of `"chill"`, the system scores it as zero, it does not understand that the two words mean the same thing.

---

## 7. Evaluation

Five different user profiles were tested by running the recommender and checking if the results made sense. For profiles like "Chill Lofi" and "High-Energy Pop," the top songs matched the genre, mood, and energy level. The most surprising result was when a "country" user was tested and the system returned indie pop songs, because there were no country songs in the catalog. A second test was run where the genre weight was cut in half and the energy weight was doubled, which changed the scores but not the top picks.

---

## 8. Future Work

- Add more songs per genre so niche listeners get better results.
- Use fuzzy mood matching so words like "mellow" and "chill" are treated as the same.
- Add a diversity rule so the top 5 results are not all from the same genre.

---

## 9. Personal Reflection

I learned that a recommender system is just a set of rules that compare numbers. The hardest part was deciding how much each feature should matter. I also learned that the data matters as much as the algorithm. If the catalog is too small or unbalanced, the results will always be limited no matter how good the scoring logic is.
