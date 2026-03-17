# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the hints were backwards").

### Bugs I Found

1. **Game starts with 1 attempt already used**
   The sidebar shows "Attempts allowed: 6" for Easy, 8 for Normal, 5 for Hard. I expected the game to start fresh with all attempts available. What actually happened: the attempt counter already showed 1 used before I made any guess, so I lost one attempt the moment the game loaded.

2. **Hints are reversed**
   I expected: guess too high → told to go lower; guess too low → told to go higher. What actually happened: when I guessed above the secret number, the message said "Go HIGHER!" and when I guessed below it, it said "Go LOWER!" — the opposite of what is correct.

3. **New game button does not actually reset the game**
   I expected clicking "New Game" to fully restart: fresh score, fresh attempts, fresh history, and a playable game. What actually happened: if I had already won or lost, clicking New Game still showed "You already won" or "Game over" and would not let me make new guesses.

4. **The in-game range prompt never updates when you change difficulty**
   I expected the text inside the game to tell me the correct range for whichever difficulty I selected. What actually happened: the prompt always read "Guess a number between 1 and 100" regardless of difficulty. This is purely a display problem — the game is showing me the wrong instructions.

5. **Game ends too early**
   I expected Normal difficulty to give me 8 real guesses. What actually happened: I only got 7 guesses before the game ended, one short of the 8 shown in the sidebar.

6. **Score does not subtract equally for each wrong guess**
   I expected every wrong guess to deduct the same number of points. What actually happened: some wrong guesses actually added points to my score instead of subtracting, and the amount changed between attempts with no consistent pattern.

7. **Hard difficulty is easier to win than Normal**
   I expected Hard to be harder than Normal — a wider range, fewer attempts, or both. What actually happened: Hard has a smaller number range than Normal, which means fewer possible numbers to guess from and the game is statistically easier on Hard than on Normal.

8. **Starting a new game generates a secret number that does not match the selected difficulty**
   Even if the display were fixed to show the right range, the actual number being generated is a separate problem. I expected the new game to pick a secret that fits within the selected difficulty. What actually happened: the new game always pulled from the same fixed pool regardless of which difficulty was active. On Easy, the secret could be a number like 87 — a number I would never reach by guessing within the range the game told me to use.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
