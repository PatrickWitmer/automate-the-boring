Practice Questions
  1.  What is []?
  well it's brackets, but I think you are asking me if it's a list, which it is.

  2.  How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
  ```
  spam = [2, 4, 6, 8, 10]
  spam[2] = 'hello'
  ```

For the following three questions, assume spam contains the list ['a', 'b', 'c', 'd'].

  3.  What does spam[int(int('3' * 2) // 11)] evaluate to?
  I have no fucking clue what kind of question is this?
  ```
  '3' * 2       # '33'
  int('33')     # 33
  33 // 11      # 3
  int(3)        # 3
  spam[3]       # 'd'  (since spam = ['a','b','c','d'])
  ```

  4.  What does spam[-1] evaluate to?
 'd'

  5.  What does spam[:2] evaluate to?
  ['a', 'b']

For the following three questions, assume bacon contains the list [3.14, 'cat', 11, 'cat', True].

  6.  What does bacon.index('cat') evaluate to?
    1

  7.  What does bacon.append(99) make the list value in bacon look like?
  [3.14, 'cat', 11, 'cat', True, 99]

  8.  What does bacon.remove('cat') make the list value in bacon look like?
  [3.14, 11, 'cat', True]
  Only removes the first reference of 'cat'

  9.  What are the operators for list concatenation and list replication?
  + for concatenation
  * for replication

  Example:

  [1, 2] + [3, 4]   # [1, 2, 3, 4]
  [1, 2] * 3        # [1, 2, 1, 2, 1, 2]

10.  What is the difference between the append() and insert() list methods?
  append(x) adds the value x to the end of the list.
  insert(i, x) adds at specific index (not always the beginning — only if you pass 0).

11.  What are two ways to remove values from a list?
  del and remove()

12.  Name a few ways that list values are similar to string values.
  They both have index values
  They can be assigned to a variable
  Are sequences (can be indexed and sliced)
  Support len()
  Can be iterated over in loop

13.  What is the difference between lists and tuples?
  lists are in [] and mutable
  tuples are in () and are immutable

14.  How do you write the tuple value that has just the integer value 42 in it?

  (42,)

15.  How can you get the tuple form of a list value? How can you get the list form of a tuple value?
  the methods tuple() and list()
  tuple([1, 2, 3])
  list((1, 2, 3)) 

16.  Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
  references to the list object in memory.

17.  What is the difference between copy.copy() and copy.deepcopy()?

  copy just copies a list, deepcopy also copies nested lists.

  copy.copy() → shallow copy (top-level only)

  copy.deepcopy() → deep copy (copies nested objects too)