class employee:
    start="10am"
    end="6 pm"
class teacher(employee):
    def __init__(self,subject) :
        self.subject=subject

t1=teacher("math")
print(t1.subject,t1.start,t1.end)
        