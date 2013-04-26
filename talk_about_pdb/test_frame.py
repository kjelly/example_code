import sys
def fun1():
    frame = sys._getframe()
    print 'this is fun1',
    print 'the frame id is ', id(frame),
    print 'the parrent of the frame is ', id(frame.f_back)

def fun2():
    frame = sys._getframe()
    print 'this is fun1',
    print 'the frame id is ', id(frame),
    print 'the parrent of the frame is ', id(frame.f_back)

    fun1()

frame = sys._getframe()
print 'this is fun1',
print 'the frame id is ', id(frame),
print 'the parrent of the frame is ', id(frame.f_back)

fun2()

