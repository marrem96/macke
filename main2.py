
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

    print(i + i + i)


#ADDED SOME DUMMY CODE HERE

#ADDED SOME SECOND DUMMY CODE HERE

#CHANGED THIRD DUMMY DATA ROW

#ADDED A FOURTH DUMMY SENTENCE

#ADDED A FIFTH DUMMY SENTENCE

#ADDED A SIXTH DUMMY SENTENCE

#ADDED A SEVENTH ROW ON MASTER

print(3+3)

#ADDED SOME THINGS ON MASTER

#ADDED BLBLBLBL ON FEATURE