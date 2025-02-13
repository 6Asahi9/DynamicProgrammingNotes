### 🧠 Mindset Behind "Replace" (Compared to Insert & Delete)
Now that you understand Insert and Delete, let’s see how Replace fits in.

### 1️⃣ Replace Mindset (Change a character to match the target)
* In Insert, we were adding characters to match word2.
* In Delete, we were removing characters to match word2.

Replace is different: Instead of adding/removing, we modify the character directly.

Example: Convert "cat" → "bat"
'c' doesn’t match 'b' → Replace 'c' with 'b' → "bat" ✅

👉 Key idea:
Instead of inserting or deleting, what if we just change the character instead?
Formula:

dp[i][j]=1+dp[i−1][j−1]

It looks diagonally (previous row and column).

![](/images/image_2025-02-13_210209330.png)

### 💡 Why Would You Use Replace?
* Insert is adding, Delete is removing, but Replace is a shortcut.
* Sometimes, replacing one character is cheaper than deleting and inserting separately.
* It’s useful when the characters are almost the same, but just slightly different.
