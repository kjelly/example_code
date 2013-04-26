import sys

class MyTraceCls(object):
    def __init__(self):
        self.count = 0

    def my_f_trace(self, frame, event, args):
        self.count += 1
        print 'trace obj count: ', self.count
        return self.my_f_trace

def my_f_trace(frame, event, args):
    print event, frame.f_lineno
    # why does it need to return self?
    return my_f_trace


def my_trace():
    frame = sys._getframe().f_back
    frame.f_trace = my_f_trace 
    trace_object = MyTraceCls()
    sys.settrace(trace_object.my_f_trace)

def fun2():
    print 'ss'

def fun1():
    my_trace()
    frame = sys._getframe()
    print frame.f_trace
    a = 1
    a += 1
    fun2()
    sys.settrace(None)
    print a
    print frame.f_trace

fun1()
