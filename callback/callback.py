def call_after(func):
    def wrapper(wrapped_func):
        def inner_wrapper():
            func()
            wrapped_func()
        return inner_wrapper
    return wrapper

def update_counter():
    print 'update counter'

@call_after(update_counter)
def demo_func():
    print 'do something'


demo_func()
