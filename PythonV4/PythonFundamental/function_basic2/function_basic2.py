def  countdown(num):
    newList = []
    for i in range(num, -1,-1):
        newList.append(i)
    return newList
print(countdown(5))


def printreturn(list):
    print(list[0])
    return list[1]
print (printreturn([5,8]))


def firstpluslength(list):
   
    return  list[0]+len(list)

print(firstpluslength([4,5,6,7,8,10,15]))


def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = []
    
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([11,5,4,6,7,1,]))


def length_value(size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(length_value(5,4))
print(length_value(7,2))
