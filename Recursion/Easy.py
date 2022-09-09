#factorial

def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)

 #fib

 def fib(n):
    if n<=1:
        return n
    
    else:
        return fib(n-1)+fib(n-2)