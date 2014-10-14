Stack traces for python
-----------------------

Traps a signal (by default, `SIGUSR1`) and writes all of the active threads' stack traces to some output (by default, `stdout`). Simple enough.

You'd plug this into your app using something like:

    if __name__ == '__main__':
        import pythonstack
        pythonstack.load()

And then you'd trigger the output something by doing something like this:

    $ python example.py &
    [1] 12345

    $ kill -s SIGUSR1 12345
    Threads at 2014-10-14T14:00:33.336161:
    --------------------------
    example.py line 14 (some_silly_method)
    example.py line 10 (run)
    /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py line 808 (__bootstrap_inner)
    /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py line 781 (__bootstrap)

    /tmp/pythonstack.py line 14 (print_stack_to_file)
    /tmp/pythonstack.py line 25 (handler_function)
    example.py line 15 (<module>)

    $

