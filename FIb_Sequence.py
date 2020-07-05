#Fibonacci Series
n=input("Enter a number");
n=int(n);
i=2;
fib=[None]*(n);
print(fib);
fib[0]=0;
fib[1]=1;
print(fib[0]);
print(fib[1]);
while i<n:
    fib[i]=fib[i-1] + fib[i-2];
    print(fib[i]);
    i+=1;

    
