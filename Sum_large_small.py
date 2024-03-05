from array import *
a=array('i',[])
n=int(input("Enter number of elements:"))
print("Enter array elements:")
for i in range(n):
    a.append(int(input()))
sum=0
for i in range(n):
    sum=sum+a[i]
large=small=a[0]
for i in range(1,n):
    if large<a[i]:
        large=a[i]
    if small>a[i]:
        small=a[i]
print("Array elements are:")
for i in range(n):
    print(a[i],end="")
print()
print("Sum of array elements:",sum)
print("Largest element in the array:",large)
print("Smallest element in the array:",small)
