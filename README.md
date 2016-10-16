# stopwatch
Basic stopwatch class to calculate time for code to complete in Python 3.5.

* Written by Mohammad Laif [Droid Programming](droidprogramming.com).
* Licensed under The [MIT License](../master/LICENSE).


## Version
**1**


## Requirement
* Python 3.5+


## Install
* git clone https://github.com/mzdhr/stopwatch.git
* copy stop_watch.py to your project directory.


## Usage
1. Create an object from file class "stop_watch.py"
2. Start that object where you want to measure time, then stop it where you want the measure to stop.

## Examples
Normal way:
```
eye = StopWatch('Bad Rabbit')
eye.start()
# blocks of codes
eye.end()
```

As a context:
```
with StopWatch('Context Manager') as eye:
    #blocks of codes
```

* Note: if you don't write a title for it, it will use the function name automatically as a title if its inside a function.

## More Example
* There are many ways to use it, for more see the test file: test_stop_watch.py.
