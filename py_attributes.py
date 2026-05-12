# class student:
#     college_name="abc college"#class
#     subject="python"
#     def __init__(self,name,gpa):#instance
#         self.name= name
#         self.gpa=gpa
# stu1=student("aman",8.5)    
# print(stu1.name)
# print(stu1.gpa)
# print(student.college_name)
# print(stu1.college_name )            

class laptop:
    storage_type="ssd"
    def __init__(self,name,ram,storage):
        self.ram=ram
        self.name=name
        self.storage=storage
    @classmethod    
    def get_storage_type(cls):
        print(f"storage type is {cls.storage_type}")  
    @staticmethod
    def discount(price,discount):
        final_price = price-(discount*price/100)  
        print(f"the discounted price is {final_price}")    

    def get_info(self):
        print(f"{self.name} has {self.ram} RAM & {self.storage} ROM {self.storage_type} cofiguration")
l1=laptop("acer","16 GB","512 GB")
l2=laptop("dell","4","256")
# l1.get_storage_type()
# l1.get_info()
# l2.get_info( )
l1.discount(40_000,10)


        