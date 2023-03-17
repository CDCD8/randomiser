import random

firstnum = (random.randint (0, 99))
secondnum = (random.randint (0, 99))

if firstnum == secondnum:
    secondnum =+ 2
thirdnum = (random.randint (1, 99))
if thirdnum == secondnum or firstnum == thirdnum:
    thirdnum =+ 1

print (firstnum, secondnum, thirdnum)

