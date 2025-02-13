### 🧠 Mindset Behind "Delete" (Compared to Insert)
Let’s compare Insert and Delete side by side to understand their thought process.

### 1️⃣ Insert Mindset (Build the target step by step)
You start with word1 and want to add characters until it becomes word2.

### Example: Convert "t" → "cart"
Step-by-step thinking:
* 't' doesn’t match 'c' → Insert 'c' → "ct"
* 't' doesn’t match 'a' → Insert 'a' → "cat"
* 't' doesn’t match 'r' → Insert 'r' → "cart"
* 't' matches 't' → ✅ Done

👉 Key idea: Look at the left (previous column) → "What if I just added one more character?"
Formula:

dp[i][j]=1+dp[i][j−1]

### 2️⃣ Delete Mindset (Trim down word1 step by step)
Now you start with word1 and want to remove characters until it matches word2.

### Example: Convert "cart" → "t"
Step-by-step thinking:
* 'c' doesn’t match 't' → Delete 'c' → "art"
* 'a' doesn’t match 't' → Delete 'a' → "rt"
* 'r' doesn’t match 't' → Delete 'r' → "t"
* 't' matches 't' → ✅ Done

👉 Key idea: Look above (previous row) → "What if I just removed one character?"
Formula:

dp[i][j]=1+dp[i−1][j]

📝 Comparison of Thought Process

![](/images/image_2025-02-13_205846236.png)

### 💡 Why Is Delete Different from Insert?
* Insert → You are adding characters to match word2.
* Delete → You are removing characters from word1.
They are like mirror images of each other!
