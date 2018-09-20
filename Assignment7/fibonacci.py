def fibo(howManyNumbers):
   if howManyNumbers == 1:
      return 1      
   else:                      
      return fibo(howManyNumbers-1) + fibo(howManyNumbers-2)

n = int(input("Input the length of Fibonacci sequence (n>=1): "))

