
def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)
    print(i)

print("****")
for i in mygenerator:
    print(i)