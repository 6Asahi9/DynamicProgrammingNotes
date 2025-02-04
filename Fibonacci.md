Start by looking at the very end of the tree, as we know the numbers less than or equal to 2 returns as 1

![](/images/image_2025-02-04_111735440.png)

by looking at this base case , we can say that numbers at the end of the tree (children)

gets returned as 1 to their parent

### Left children 
1. parent 3 has two children 2 and 1, both gets returned as 1 and gets added so 3 gives value 2
2. parent 4 has two children 3 and 2, 3 gives value 2 and 2 gives value 1, sum = 3
3. parent 5 has two children 4 and 3, 4 gives value of 3 and 3 gives value of 2, sum = 5
4. parent 6 has two children 5 and 4, 5 gives value of 5 and 4 gives value of 3, sum = 8
5. root parent 7 has two children 6 and 5, 6 gives value of 8 and 5 gives value of 5, sum = 13
