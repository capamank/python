class employee:
    start="10am"
    end="6 pm"
    def change_time(self,time):
        self.end=time
class teacher(employee):
    def __init__(self,subject) :
        self.subject=subject
class admin(employee):
    def __init__(self,role):
        self.role=role
class accountant(admin):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary        
t1=teacher("math")
t2=teacher("geography")
staff1=admin("manager")
acc1=accountant(29307,"CA")
t1.change_time("5pm")
 
print(acc1.role,acc1.salary) 

print(t1.subject,t1.start,t1.end)

print(staff1.role,staff1.start,staff1.end) 
print(t2.end)       