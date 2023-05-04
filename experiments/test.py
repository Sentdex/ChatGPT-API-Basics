g1 = (x*x for x in range(10))

def g2():
    for x in range(10):
        yield x*x
# g1 = g2()

print(type(g1))
print(next(g1))
print(next(g1))