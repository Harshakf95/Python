def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    n=int(input("Enter value for n: "))
    print("First",n,"Fibonacci series are:")
    for i in range(n):
        print(fibo(i),end="")