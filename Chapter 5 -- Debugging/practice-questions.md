Practice Questions
  1.  Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

  assert spam < 10

  2.  Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different. (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'.)

  eggs = "goodbye"
  bacon = "GOODbye"
  assert eggs.lower() != bacon.lower()

  3.  Write an assert statement that always triggers an AssertionError.

    assert False

  4.  What two lines must your program have to be able to call logging.debug()?
```
  import logging
  logging.basicConfig(level=logging.DEBUG)
```

  5.  What two lines must your program have to make logging.debug() send a logging message to a file named programLog.txt?
```
  import logging
  logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```

  6.  What are the five logging levels?

  Can't recall all but maybe some of these.
  Debug
  INFO
  WARNING
  ERROR
  CRITICAL

  7.  What line of code can you add to disable all logging messages in your program?


  `logging.disable(logging.CRITICAL)`
  This disables everything at CRITICAL and below (i.e., everything).

  8.  Why is using logging messages better than using print() to display the same message?

  Because you can toggle them on and off and not have to manually remove them when you don't need them anymore.

  Extra:
    Logging can be set to different levels.
    Logging can write to files automatically.
    Logging is thread-safe and works better in big program

  9.  What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

  This is mu stuff and I don't care I'm not using Mu. Convince me otherwise (vs code debugger?)

10.  After you click Continue, when will the debugger stop?
  This is mu stuff and I don't care I'm not using Mu. Convince me otherwise (vs code debugger?)

11.  What is a breakpoint?
This is mu stuff and I don't care I'm not using Mu. Convince me otherwise (vs code debugger?)

12.  How do you set a breakpoint on a line of code in Mu?
This is mu stuff and I don't care I'm not using Mu. Convince me otherwise (vs code debugger?)

We can do all this in VS Code:

1. Learn VS Code
Why: It’s the most popular code editor in the world.

Skills to learn:

Installing Python extension

Running Python scripts in VS Code

Using the built-in debugger (Step Over, Step In, breakpoints)

Setting up virtual environments (python -m venv venv)

