# Chapter 4 Testicals

## Practice Questions
  1.  Why are functions advantageous to have in your programs?
  Because you can compartmentalize your code into blocks or "black boxes" to call back with parameters and arguments.

  2.  When does the code in a function execute: when the function is defined or when the function is called?
  When it is called later in the code.


  3.  What statement creates a function?
  def

  4.  What is the difference between a function and a function call?
  A function is block of code to execute.
  A function call is a line of code to initiate the block of code execution.

  5.  How many global scopes are there in a Python program? How many local scopes are there?
  There is only one global scope.
  There are as many local scopes as you need.

  6.  What happens to variables in a local scope when the function call returns?
  It gets fucked. G Fucked. (Is deleted)

    😆 Mostly correct, technically speaking:
More accurate phrasing:

Local variables are destroyed when the function exits—Python frees that memory automatically.

So yes: G-f'd by the garbage collector

  7.  What is a return value? Can a return value be part of an expression?
  A return value is the value returned by the function.
  Yes you can

  8.  If a function does not have a return statement, what is the return value of a call to that function?
  I don't know 

    🧠 Correct answer:
If there is no return statement, the function returns None by default.

  9.  How can you force a variable in a function to refer to the global variable?
  In the local scope use the statement:
   global variable

10.  What is the data type of None?
  Boolean?

  ❌ Incorrect.
None is its own data type: NoneType.
It's often used to represent "no value," but it’s not Boolean.

11.  What does the import areallyourpetsnamederic statement do?
  What in the fuck did you just say to me Al?
  it imports the imaginary module, areallyourpetsnamederic.

12.  If you had a function named bacon() in a module named spam, how would you call it after importing spam?
  import spam

  breakfast = spam.bacon()

13.  How can you prevent a program from crashing when it gets an error?
  Use try and except statments?

14.  What goes in the try clause? What goes in the except clause?
  The loop goes in the try clause, the error expection or sys.exit() goes in the expect clause

15.  Write the following program in a file named notrandomdice.py and run it. Why does each function call return the same number?

import random
random_number = random.randint(1, 6)

def get_random_dice_roll():
    # Returns a random integer from 1 to 6
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())

  This is a scope issue, we need to move random_number into the function so it is a local variable.