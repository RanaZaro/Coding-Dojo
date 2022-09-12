
i = 0
while i <=150:
    print (i)
    i+=1

n = 5
while n <1001:
     print(n)
     n=n+5

for z in range(101):
  if z%10==0:
      print("coding dojo") 
       
  if z%5==0 and z%10!=0:
      print("coding")

      sum=0
for i in range(0,500001):
    if i%2!=0:
    	sum=sum+i
print(sum)


def countdown(i):
	while i > 0:
		print(i)
		i=i-4
		if i ==0:
			break
countdown(2018)


lownum=2
highnum=9
mult=3

for t in range(lownum,highnum+1):
    if t % mult==0:
        print(t)
