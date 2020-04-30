def outer_func():
    print('Call outer_func function')

    def inner_func():
        return 'call inner_func function'

    print(inner_func())
outer_func()