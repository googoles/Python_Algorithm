def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

g = get_natural_number()

for _ in range(0, 100):
    print(next(g))



