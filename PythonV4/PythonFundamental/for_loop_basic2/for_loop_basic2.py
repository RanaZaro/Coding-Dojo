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


def minimum(arr):
    minimum=arr[0]
       if len(arr)<1:
       return False
 
   
    for i in range(len(arr)):
		    if minimum>arr[i]:
		        minimum=arr[i]

    print(minimum)

minimum([37,2,1,-9])
minimum([])


def maximum(arr):
   max=arr[0]
   
    if len(arr)<1:
		    return False
    for i in range(len(arr)):
        if max<arr[i]:
        	max=arr[i]
    print(max)
maximum([37,2,1,-9])
maximum([])


def ultimate(arr):
    min=arr[0]
    max=arr[0]
    total=0
    i=0
    for i in range(len(arr)):
        if min > arr[i]:
        	min=arr[i]
        if max < arr[i]:
        	max=arr[i]
        total+=arr[i]
    avg=total/len(arr)
    length=len(arr)
    print(min)
    print(max)
    print(total)
    print(avg)
    print(length)

ultimate([37,2,1,-9])






    

    

    

