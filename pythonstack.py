import datetime
import os
import signal
import sys


def print_stack_to_file(output=sys.stdout):
    timestamp = datetime.datetime.now().isoformat()
    header = '-' * len(timestamp)
    pid = os.getpid()
    output.write('Threads for %s at %s:\n%s\n' % (pid, timestamp, header))
    for f in sys._current_frames().values():
        while f is not None:
            c = f.f_code
            output.write('%s line %d (%s)\n' % (
                c.co_filename, f.f_lineno, c.co_name))
            f = f.f_back
        output.write('\n')
    output.flush()


def load(sig=signal.SIGUSR1, output=sys.stdout):
    old_handler = signal.getsignal(sig)

    def handler_function(signal_num, interrupted_frame):
        if hasattr(old_handler, '__call__'):
            old_handler(signal_num, interrupted_frame)
        print_stack_to_file(output)
    return signal.signal(sig, handler_function)
