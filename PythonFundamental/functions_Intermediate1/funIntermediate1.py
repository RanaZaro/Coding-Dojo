import random
def randInt():
    print(int(random.random()*100))
randInt()

import random
def randInt2():
    print(int(random.random()*50))
randInt2()


import random
def randInt3():
    print(round(random.random()*100 + 50))
randInt3()


import random
def randInt4(min,max):
    print(round(random.random()*max+min))
randInt4(50,500)