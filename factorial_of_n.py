# write  a function to print factorial of a number

def fun(n):
     fact = 1
     for i in range(1,n+1):
        fact *= i
     return fact   
        
ans=fun(10)    
print(ans)
