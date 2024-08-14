def lcm(a, b):
    i = max(a, b)
    while True:
        if i % a == 0 and i % b == 0:
            return i
        i += max(a, b)


print(lcm(15, 20))
