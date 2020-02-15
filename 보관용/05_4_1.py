class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("nono")












# class Bird:
#     def fly(self):
#         raise NotImplementedError
#
# class Eagle(Bird):
#     def fly(self):
#         print("very fast")
# eagle = Eagle()
# eagle.fly()
