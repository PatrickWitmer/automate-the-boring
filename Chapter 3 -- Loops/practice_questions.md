# Practice Questions
 
1.  What keys can you press if your Python program is stuck in an infinite loop?
  
  ctrl+c

2.  What is the difference between break and continue?

  break exits the entire loop immediately.

  continue skips the rest of the current iteration and goes to the next loop cycle.

3.  What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

  range(10) = will iterate 0-9
  range(0, 10) = will iterate 0-9
  range(0, 10, 1) = same as the last example. 0-9

   You could clarify:

    range(10) → starts at 0, goes to 9 by default

    range(0, 10) → explicitly starts at 0

    range(0, 10, 1) → explicitly starts at 0 and steps by 1

4.  Write a short program that prints the numbers 1 to 10 using a for loop. Then, write an equivalent program that prints the numbers 1 to 10 using a while loop.

  ```
  for i in range(1, 11):
    print(i)
  ```

  ```
  count = 1
  while count < 11:
    print(count)
    count += 1
  ```  

5.  If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

  spam.bacon()