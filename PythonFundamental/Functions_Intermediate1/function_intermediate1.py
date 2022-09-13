import random
def randInt():
    print(int(random.random()*100))
randInt()

import random
def randInt2():
    print(int(random.random()*20))
randInt2()


# import random
# def randInt(min=   , max=   ):
#     num = random.random()
#     return num
# print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500



# import random
# def randInt3(0,300):
#     # values = list(range(0,300))
#     print(int(random.random(0,300)))
# randInt3()

# import random
# def randInt4 ( min=    , max=  ):
#     values = list(range(20,100))
#     print(int(random.random(values)))
# randInt4()

# import random
# def randInt5():
#     values = list(range(20,300))
#     print(int(random.random(values)))
# randInt5()


import random
def randInt3(min=50,max=100 ):
    
         num = random.random()
         return num
print(randInt(max=50)*100) 
