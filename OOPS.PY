class student:
    sub="python"
    college="abx college"
    year="2nd year"

student1=student()
student2=student()
print(student1.sub,student1.college,student1.year)
print(student2.sub,student2.college,student2.year)

class kid:
    def __init__(self,name,school):#parameterized
        self.name=name
        self.school=school
    def  get_school(self):#defaut constructor
        return self.school
        
car1=kid("aman","red")
car2=kid("xavier","blue")
car3=kid("gandu","green")
# print(car1.name)
# print(car2.name)
# print(car3.name)
# print(car1.school)
# print(car2.school)
# print(car3.school)
print(f"{car1.name} has color of {car1.get_school()}")


        
        
        




        
        

