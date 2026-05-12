# Write a program that takes  as input. Using conditional statements, 
# calculate the  
# final tax rate
# based on these rules:
# • 
# If salary < 30,000 → 5%
# • 
# If salary is 30,000–70,000 → 15%
# • 
# If salary > 70,000 → 25%
sal=int(input("enter your salary="))
if sal<=30000:
    print("tax is 5%")
elif sal<=70000:
    print("tax is 15%")
else:
    print("tax is 25%")    
    
    