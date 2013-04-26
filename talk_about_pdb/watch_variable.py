import sys
import pdb

class WatchDict(object):
    def __init__(self, variable, expected_data):
        self.variable = variable
        self.expected_data = expected_data

    def trace_change(self, frame, event, args):
        for i in self.expected_data:
            if i in self.variable:
                if self.variable[i] != self.expected_data[i]:
                    pdb.set_trace()
                    return sys._getframe().f_back.f_trace
            else:
                pdb.set_trace()
                return sys._getframe().f_back.f_trace
        return self.trace_change
    
    @staticmethod
    def create_watch_dict(variable, expected_data):
            watch_dict = WatchDict(variable, expected_data)
            frame = sys._getframe().f_back
            while frame:
                frame.f_trace = watch_dict.trace_change
                frame = frame.f_back
            sys.settrace(watch_dict.trace_change)


def fun1():
    a = 1
    b = 1
    WatchDict.create_watch_dict(locals(), {'a': 1})
    b += 1
    b += 1
    b += 1
    b += 1

fun1()
