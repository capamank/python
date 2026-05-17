try:
    x=int(input("enter a number"))
    ans=10/x
except ZeroDivisionError:
   print("division with 0 is not allowed")   
except ValueError:
   print("you have to enter a valid number")   
else:
   print(f"answer is {ans}")

finally:
   print("this is the end of our python program ")
   


    
    
    
    