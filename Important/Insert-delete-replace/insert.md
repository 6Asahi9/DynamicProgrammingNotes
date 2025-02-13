Exactly! If characters are equal, use diagonal (top-left) value.
If not equal, we insert → Take left value and add +1. ✅

### How Did Someone Think of This? (Their Mindset)
Great question! Let’s reverse-engineer their thought process. Imagine you're solving this problem from scratch without knowing DP.

### Step 1: Think Brute Force First (Recursive Thinking)
If I manually transform "t" → "cart", what are my options?

1. 't' doesn’t match 'c' → Insert 'c' before 't'
* "ct" (1 operation)
2. 't' doesn’t match 'a' → Insert 'a'
* "cat" (2 operations)
3. 't' doesn’t match 'r' → Insert 'r'
* "cart" (3 operations)
4. 't' matches 't', so no need to insert! ✅
* Final word: "cart" (3 insertions).

### Step 2: Noticing the Pattern
Each time I insert, I only need to look at what’s missing and keep moving forward.

* "c" is missing → Add 1 to previous solution.
* "ca" is missing → Add 1 to previous solution.
* "car" is missing → Add 1 to previous solution.
### 🧠 Key Insight:
* To form "car", I only needed to take "ca" and add 'r'.
* To form "ca", I only needed to take "c" and add 'a'.

So instead of recomputing from scratch, I can store previous results and just add +1 each time.

### Step 3: Turning This into a Formula
Since inserting only depends on the previous column (left side), we generalize it:

dp[i][j] = 1+dp[i][j−1]

Meaning:

* "Look at the smaller version of the problem" (word1 → word2[:j-1])
* "Just add 1 for the new character"
Now it makes sense, right? 😆 They weren’t randomly coming up with a formula—they just recognized a repeating pattern and turned it into math!

📝 Summary of Mindset
Try brute force manually.
Look for a repeating pattern in smaller cases.
Realize you can build a solution step-by-step.
Generalize it into a DP formula.
This is how all DP solutions are born! Someone struggled manually, noticed a pattern, and then optimized it with memory. 😆

