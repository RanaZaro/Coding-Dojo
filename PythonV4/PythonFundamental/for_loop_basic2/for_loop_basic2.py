def biggie_size(arr):

    for i in range(len(arr)):
         if arr[i] > 0:
            arr[i] = "big"

    return arr   

print(biggie_size([-1,5,-2,6,8,7,-6]))


def countPositive(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]>0:
            count+=1
    arr[len(arr)-1]=count

   
    
    print(arr)

countPositive([-1,1,1,1])
countPositive([1,6,-4,-2,-7,-2])


def sumTotal(arr):
	sum=0
	for i in range(len(arr)):
		sum+=arr[i]
	print(sum)

sumTotal([1,2,3,4])
sumTotal([6,3,-2])



def average(arr):
    total=0
    avr=0
    for i in range(len(arr)):
        total+=arr[i]
    avr=total/len(arr)
    print(avr)

average([1,2,3,4])  
average([1,2,3,10])  



def length(arr):
	length_arr=len(arr)
	print(length_arr)
  
length([37,2,1,-9])
length([])


def minimum (list):
   if len(list)>0:
    min = list[0]
    for i in range (len (list)):
        if list[i]<min:
            min= list[i]
    return min
   else:
    return False

print(minimum([1,6,-9,8]))
print(minimum([]))


minimum([37,2,1,-9])
minimum([])


def maximun (list):
    if len(list)>0:
        max = list[0]
        for i in range (len(list)):
            if list[i]>max:
                max = list[i]
        return max
    else:
        return False 
print (maximun([37,2,1,-9]))
print (maximun([]))



def ultimate(list):
    min = list[0]
    max = list[0]
    sum = 0
    avg = 0
    for i in range (len(list)):
        if list [i]<min:
            min = list[i]
        if list[i]>max:
            max = list[i]
        sum = sum + list[i]
        avg = sum/len(list)
        length = len(list)

    print("minimum number is " + str(min))
    print("maximum number is " + str (max))
    print ("total value is " + str (sum))
    print ("average number is " + str (avg))
    print ("list length is " + str (length))

ultimate([37,2,1,-9])



def reverse (list):
    for i in range (0, len(list)//2):
        temp = list[i]
        list[i] = list[len(list)-i-1]
        list[len(list)-i-1]= temp
    return list

print (reverse([37,2,1,-9]))






    

    

    

