class bank_account:
    def __init__(self,name,balance,password):
        self.name=name#public
        self._balance=balance#protected
        self.__password=password#private

    def get_password(self):
         return self.__password
        
acc1=bank_account("aman",1000,"skdlghskj")
print(acc1.name,acc1._balance,acc1.get_password())
        