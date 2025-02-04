![](/images/image_2025-02-04_142551474.png)

Lets say we have a grid of 3 rows and 3 columns 
now if we look at this we have two ways to go from starting point

* Down

![](/images/image_2025-02-04_142727836.png)

and as you can we can cut the first row and now work of it like if it was a grid of 2 rows and 3 columns 

we can even cut it again in (2,2)

![](/images/image_2025-02-04_142847740.png)

we can keep cutting it until we have a (1,1) or the base case 

### Graph

Just like Fibonacci , we'll keep going until we reach the base case and come back to the parent after adding the child

![](/images/image_2025-02-04_143128775.png)

![](/images/image_2025-02-04_143303684.png)

and we keep doing it until we reach the root which will give us the answer 3
