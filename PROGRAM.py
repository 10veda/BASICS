# basic-programcls


*************************Salary Increment by holding a single value*****************
n=list(map(int,input().split()))
m=min(n)
while True:
    x=n.index(max(n))
    for i in range(len(n)):
        if i!=x:
            n[i]+=1
    if len(set(n))==1:
        print(n[0]-m)
        break
        
        o/p
         ==================
5 1 2 4 3
10
**************************Bubble sort**********************

a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(len(a)-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
for i in range(len(a)):
    print(a[i],end=" ")
    
o/p:
    5 7 2 8 1
    1 2 5 7 8 
    
   *******************Selection sort********************
a=list(map(int,input().split()))
for i in range(len(a)):
    min=i
    for j in range(i+1,len(a)):
        if(a[j]<a[min]):
            min=j
    a[i],a[min]=a[min],a[i]
for i in range(len(a)):
    print(a[i],end=" ")
        

o/p:
5 7 2 8 1
1 2 5 7 8 

**********************Insertion sort***********************

a=list(map(int,input().split()))
for i in range(len(a)):
    j=i
    while j>0:
        if a[j]<a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
            j=j-1
        else:
            break
print(a)


o/p:
 3 4 5 2 1
 1 2 3 4 5
 ***********************count the number of 1's in buinary num**************8
n=int(input())
c=0
while n:
    n&=n-1
    c+=1
print(c)    
    
    
    o/p
    15
    4
    
 *********************print the largest palindrome in a sentence without reverdse function**********************8


str=input()
n=len(str)
slnd=elnd=0
for i in range(n):
    for j in range(n-1,i,-1):
        ind1=i 
        ind2=j 
        while ind1<ind2:
            if str[ind1]!=str[ind2]:
                break
            ind1+=1
            ind2-=1
        if ind1>=ind2:
            if j-i>elnd-slnd:
                slnd=i
                elnd=j
print(str[slnd:elnd+1])
o/p:

my madam's mother tongue is malayalam
malayalam
