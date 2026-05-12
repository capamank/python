
# Write a function that takes two integers  and  and prints all even 
# numbers between them (inclusive).
a=int(input("enter A="))
b=int(input("enter B="))
for i in range(a,b):
    if i%2==0:
        print(i)