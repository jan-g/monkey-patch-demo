# Monkey-patching to trace `open` calls

The module `_mp` (you might want to rename it) fiddles with the `__builtins__` dictionary. It does
this to replace the `open` builtin function with an implementation that wraps it.

You can manually insert a line:

    import _mp

at the start of your program's entry-point before invoking it. What you'll get as a result is
the same program, but you get to intercept all calls to `open` and decide what to do with them.

You can print out a stack trace (as here); or drop into a debugger, or what-have-you.
